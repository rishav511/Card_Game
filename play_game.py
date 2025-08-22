import random
import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from draw_a_card import Deck
from player_strategy import FaceValuePlayer, RandomPlayer, OpponentAwarePlayer, OpponentAwareStrategicPlayer, UserPlayer
from performance import analyze_performance
import time

console = Console()

def render_leaderboard(players, face_value, bids):
    table = Table(title=f"Card Drawn: [bold cyan]{face_value}[/bold cyan]")
    table.add_column("Player", style="bold")
    table.add_column("Bid", style="yellow")
    table.add_column("Score", style="green")

    sorted_players = sorted(players, key=lambda p: p.score, reverse=True)
    for p in sorted_players:
        table.add_row(p.name, str(bids[p.name]), f"{p.score:.2f}")
    return table

def play_game(players):
    deck = Deck()
    game_data = []

    while deck.is_deck_not_empty():
        face_value = deck.draw_a_card()
        bids = {p.name: p.play(face_value) for p in players}
        
        for p in players:
            p.update_seen(face_value)
            for opp in players:
                if opp != p:
                    opp.update_opponent(p.name, bids[p.name])
        
        max_bid = max(bids.values())
        winners = [name for name, bid in bids.items() if bid == max_bid]
        score_increment = face_value / len(winners)
        
        for p in players:
            if p.name in winners:
                p.add_score(score_increment)

        scores = {p.name: p.score for p in players}
        game_data.append({"card": face_value, "bids": bids, "scores": scores})

        table = Table(title=f"🎴 Card Drawn: [bold cyan]{face_value}[/bold cyan]", header_style="bold magenta")
        table.add_column("Player", style="bold")
        table.add_column("Bid", justify="center", style="yellow")
        table.add_column("Score", justify="center", style="green")

        for p in players:
            table.add_row(
                p.name,
                str(bids[p.name]),
                f"{p.score:.2f}"
            )

        console.print(table)

        winner_names = ", ".join(f"[bold green]{w}[/bold green]" for w in winners)
        console.print(f"[cyan]Round Winner(s):[/cyan] {winner_names}")
        console.rule()
        
        time.sleep(1)

    winner = max(players, key=lambda p: p.score)
    return winner, game_data

def choose_players(num_players, user_play):
    bot_classes = [FaceValuePlayer, RandomPlayer, OpponentAwarePlayer, OpponentAwareStrategicPlayer]
    bot_names = [f"Bot{i+1}" for i in range(len(bot_classes))]

    players = []
    if user_play:
        players.append(UserPlayer("You"))
        num_bots = num_players - 1
    else:
        num_bots = num_players

    selected = random.sample(list(zip(bot_classes, bot_names)), num_bots)
    players.extend([cls(name) for cls, name in selected])
    return players

def main():
    parser = argparse.ArgumentParser(description="🎴 Card Bidding Game")
    parser.add_argument("-n", "--num-players", type=int, choices=[2, 3], required=True, help="Number of players (2 or 3)")
    parser.add_argument("-u", "--user-plays", action="store_true", help="Include yourself as a player")
    args = parser.parse_args()

    console.print(Panel.fit("🎮 [bold magenta]Welcome to the Card Bidding Game![/bold magenta]", style="bold blue"))

    players = choose_players(args.num_players, args.user_plays)
    console.print(f"\n[bold green]Players:[/bold green] {', '.join(p.name for p in players)}")
    console.print("[yellow]Starting game...[/yellow]\n")

    winner, game_data = play_game(players)
    console.print(f"\n🏆 [bold green]{winner.name}[/bold green] wins with a score of [cyan]{winner.score:.2f}[/cyan]!")

    analyze_performance(game_data)

if __name__ == "__main__":
    main()

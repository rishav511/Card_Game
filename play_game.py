import random
import argparse
import statistics as stats
from draw_a_card import Deck
from player_strategy import FaceValuePlayer, RandomPlayer, OpponentAwarePlayer, OpponentAwareStrategicPlayer, UserPlayer
from performance import analyze_performance

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
        
        print(f"Card {face_value} | Bids: {bids}")
        for p in players:
            print(f"{p.name}: {p.score}")
        print("-" * 40)
    
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
    parser = argparse.ArgumentParser(description="Card bidding game")
    parser.add_argument("-n", "--num-players", type=int, choices=[2, 3], required=True)
    parser.add_argument("-u", "--user-plays", action="store_true")
    args = parser.parse_args()
    
    players = choose_players(args.num_players, args.user_plays)
    print(f"\nPlayers: {[p.name for p in players]}")
    print("\nStarting game...\n")
    
    winner , game_data = play_game(players)
    print(f"\n🏆 Winner: {winner.name} (Score: {winner.score})")

    analyze_performance(game_data)

if __name__ == "__main__":
    main()
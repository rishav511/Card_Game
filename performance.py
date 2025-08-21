import statistics as stats
from rich.table import Table
from rich.panel import Panel

def analyze_performance(data, console):
    if not data:
        return
    
    players = list(data[0]["bids"].keys())
    
    console.print("\n[bold magenta]📊 Final Performance Analysis[/bold magenta]")
    
    table = Table(title="Player Stats", header_style="bold blue")
    table.add_column("Player", style="bold")
    table.add_column("Mean Bid (μ)", justify="right")
    table.add_column("Bid StdDev (σ)", justify="right")
    table.add_column("Final Score", justify="right", style="green")
    table.add_column("Wins", justify="right", style="cyan")
    
    for player in players:
        bids = [round_data["bids"][player] for round_data in data]
        final_score = data[-1]["scores"][player]
        wins = sum(1 for r in data if r["bids"][player] == max(r["bids"].values()))
        
        table.add_row(
            player,
            f"{stats.mean(bids):.2f}",
            f"{stats.stdev(bids):.2f}" if len(bids) > 1 else "0.00",
            f"{final_score:.2f}",
            f"{wins}/{len(data)} ({wins/len(data)*100:.1f}%)"
        )
    
    console.print(table)
    console.print(Panel.fit("✅ Game Over — Thanks for playing!", style="bold green"))

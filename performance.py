from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track

console = Console()

def analyze_performance(data):
    players = list(data[0]["bids"].keys())
    win_count = defaultdict(int)
    bid_points = {p: defaultdict(float) for p in players}
    bid_rounds = {p: defaultdict(int) for p in players}
    score_progress = {p: [] for p in players}
    high_card_usage = {p: [] for p in players}
    low_face_high_bid = {p: 0 for p in players}
    high_face_low_bid = {p: 0 for p in players}

    for round_index, round_data in enumerate(track(data, description="Analyzing game..."), start=1):
        max_bid = max(round_data["bids"].values())
        winners = [p for p, b in round_data["bids"].items() if b == max_bid]

        for p in players:
            score_progress[p].append(round_data["scores"][p])
            bid_val = round_data["bids"][p]
            face_val = round_data["card"]

            # Points tracking
            bid_points[p][bid_val] += round_data["scores"][p] - (score_progress[p][-2] if len(score_progress[p]) > 1 else 0)
            bid_rounds[p][bid_val] += 1

            # High card usage
            if bid_val >= 10:
                high_card_usage[p].append(round_index)

            # Risk pattern detection
            if face_val <= 5 and bid_val >= 10:
                low_face_high_bid[p] += 1
            if face_val >= 10 and bid_val <= 5:
                high_face_low_bid[p] += 1

            # Win count
            if p in winners:
                win_count[p] += 1

    for p in players:
        console.print(Panel.fit(f"📊 Performance Analysis for [bold yellow]{p}[/bold yellow]", style="cyan"))

        console.print(f"[green]Final Score:[/green] {score_progress[p][-1]}")
        console.print(f"[green]Rounds Won:[/green] {win_count[p]} / {len(data)} ({(win_count[p]/len(data))*100:.1f}%)\n")

        # Table of points per card
        table = Table(title="Points Earned per Card", header_style="bold magenta")
        table.add_column("Card Value", justify="center")
        table.add_column("Total Points", justify="center")
        table.add_column("Efficiency (Points/Round)", justify="center")

        for bid_val in sorted(bid_points[p]):
            efficiency = bid_points[p][bid_val] / bid_rounds[p][bid_val] if bid_rounds[p][bid_val] else 0
            table.add_row(str(bid_val), f"{bid_points[p][bid_val]:.1f}", f"{efficiency:.2f}")

        console.print(table)

        # High card timing
        if high_card_usage[p]:
            avg_high_card_timing = sum(high_card_usage[p]) / len(high_card_usage[p])
            console.print(f"[blue]Avg timing of high card plays (10+):[/blue] Round {avg_high_card_timing:.1f}")
        else:
            console.print("[red]No high cards played (10+)[/red]")

        # Bidding pattern analysis
        console.print("\n[bold underline]Bidding Pattern Analysis:[/bold underline]")
        if low_face_high_bid[p] > 0:
            console.print(f"  ⚠ Risk-taking: Played {low_face_high_bid[p]} high bids (10+) on low face cards (≤5).")
        if high_face_low_bid[p] > 0:
            console.print(f"  🤔 Conservative: Played {high_face_low_bid[p]} low bids (≤5) on high face cards (≥10).")
        if low_face_high_bid[p] == 0 and high_face_low_bid[p] == 0:
            console.print("  🎯 Balanced: No risky or overly conservative plays detected.")

        console.print(f"\n[green]Score Progression:[/green] {' → '.join(str(s) for s in score_progress[p])}")
        console.print("\n" + "-" * 60 + "\n")
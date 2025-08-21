import statistics as stats

def analyze_performance(data):
    if not data:
        return
        
    players = list(data[0]["bids"].keys())
    
    for player in players:
        bids = [round_data["bids"][player] for round_data in data]
        final_score = data[-1]["scores"][player]
        wins = sum(1 for r in data if r["bids"][player] == max(r["bids"].values()))
        
        print(f"\n📊 {player} Performance:")
        print(f"  Bids: μ={stats.mean(bids):.2f}, σ={stats.stdev(bids):.2f}")
        print(f"  Score: {final_score:.2f}")
        print(f"  Wins: {wins}/{len(data)} ({wins/len(data)*100:.1f}%)")
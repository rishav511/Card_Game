import random 


def play_game(players):
    deck = Deck()

    while deck.is_deck_not_empty():
        face_value = deck.draw_a_card()
        bids = {}

        
        for player in players:
            bid = player.play(face_value)
            bids[player.name] = bid
            player.update_seen(face_value)
            
            for opp in players:
                if opp != player:
                    opp.update_opponent(player.name, bid)

       
        max_bid = max(bids.values())
        winners = [p for p, b in bids.items() if b == max_bid]
        if len(winners) == 1:
            for player in players:
                if player.name == winners[0]:
                    player.add_score(face_value)
        else:
            for player in players:
                if player.name in winners:
                    player.add_score(face_value / len(winners))

        print(f"Face card {face_value} | Bids: {bids}")
        for player in players:
            print(f"{player.name} score: {player.score}")
        print("-" * 40)

    
    print("\nFinal Scores:")
    for player in players:
        print(f"{player.name}: {player.score}")

    winner = max(players, key=lambda p: p.score)
    print(f"\n Winner: {winner.name}")

def choose_players():
    bot_map = {
        "Player 1": FaceValuePlayer,
        "Player 2": RandomPlayer,
        "Player 3": OpponentAwarePlayer
    }

    num_players = int(input("Hi! 2 player game or 3 player game? (Enter 2 or 3): "))
    user_play = input("Do you want to be one of the players? (yes/no): ").strip().lower()

    players = []

    if user_play == "yes":
        players.append(UserPlayer("You"))
        chosen_bots = random.sample(list(bot_map.keys()), num_players - 1)
        for bot in chosen_bots:
            players.append(bot_map[bot](bot))
    else:
        chosen_bots = random.sample(list(bot_map.keys()), num_players)
        for bot in chosen_bots:
            players.append(bot_map[bot](bot))

    return players



def main():
    players = choose_players()
    print("\nSelected Players:")
    for p in players:
        print("-", p.name)
    print("\nStarting game...\n")
    play_game(players)


if __name__ == "__main__":
    main()
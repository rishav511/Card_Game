# Card Bidding Game

A simple, text-based card bidding game implemented in Python. Players compete by bidding on cards drawn from a deck, and the player with the highest score at the end wins. The game supports multiple AI-driven player strategies and allows for performance analysis of each game session.

## Features

-   **Command-Line Interface**: Easily configure and start games using command-line arguments.
-   **Human vs. AI**: Play against different bot strategies.
-   **AI vs. AI Simulation**: Watch different AI strategies compete against each other.
-   **Multiple Bot Strategies**: Includes several distinct AI players with unique bidding logic.
-   **Performance Analysis**: After each game, view statistics on player performance, including bidding patterns and win rates.

## Requirements

-   Python 3.x

## Setup

It is highly recommended to use a Python virtual environment to manage project dependencies and avoid conflicts with system-wide packages.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repo-url>
    cd Card_Game
    ```

2.  **Create a virtual environment:**
    On macOS and Linux:
    ```bash
    python3 -m venv venv
    ```
    On Windows:
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
    Your shell prompt should now be prefixed with `(venv)`.

## How to Play

The game is run from the command line using `play_game.py`.

### Basic Commands

You must specify the number of players and whether you want to play.

-   **To play a 2-player game against a bot:**
    ```bash
    python play_game.py --num-players 2 --user-plays
    ```
    *(You can also use the short flags: `python play_game.py -n 2 -u`)*

-   **To watch a 3-player game between bots:**
    ```bash
    python play_game.py --num-players 3
    ```
    *(Short flag: `python play_game.py -n 3`)*

-   **To see all available options:**
    ```bash
    python play_game.py --help
    ```

### Gameplay

-   When a card is drawn from the deck, each player places a bid using one of the cards from their hand (1-13).
-   The player(s) with the highest bid win(s) the round.
-   The value of the drawn card is added to the winner's score. If there's a tie for the highest bid, the points are split evenly among the winners.
-   The game ends when all 13 cards from the deck have been drawn.
-   The player with the highest total score is declared the winner.

## API and Module Documentation

The project is structured into several modules, each with a specific responsibility.

### `play_game.py`

This is the main entry point for the application.

-   **`main()`**: Parses command-line arguments (`--num-players`, `--user-plays`), sets up the players, starts the game, and triggers the performance analysis at the end.
-   **`choose_players(num_players, user_play)`**: Creates a list of player objects for the game. It randomly selects from the available bot strategies. If a human is playing, it adds a `UserPlayer` instance.
-   **`play_game(players)`**: Contains the main game loop. In each round, it:
    1.  Draws a card.
    2.  Collects bids from all players.
    3.  Updates players with opponent move information.
    4.  Determines the winner(s) of the round.
    5.  Distributes points.
    6.  Prints the round's summary.
    7.  Collects data for final performance analysis.

### `player_strategy.py`

This module defines the various player types and their bidding logic. All player classes inherit from a base `Player` class.

-   **`UserPlayer`**: A player controlled by a human. It prompts the user for a bid in each round via the command line.
-   **`RandomPlayer`**: The simplest AI strategy. It bids a randomly chosen card from its hand.
-   **`FaceValuePlayer`**: A simple, predictable AI. It attempts to bid the card from its hand that has the same value as the card up for auction.
-   **`OpponentAwarePlayer`**: A more intelligent AI that tracks the cards played by opponents to inform its bidding strategy.
-   **`OpponentAwareStrategicPlayer`**: The most advanced AI strategy, using a more complex algorithm that considers the card value, its own hand, and opponent history to make optimal bids.

### `draw_a_card.py`

This module manages the game's deck.

-   **`Deck` class**:
    -   `__init__()`: Initializes a deck with 13 cards (values 1-13).
    -   `draw_a_card()`: Removes and returns a random card from the deck.
    -   `is_deck_not_empty()`: Returns `True` if there are cards left in the deck, `False` otherwise.

### `performance.py`

This module provides functionality to analyze a completed game.

-   **`analyze_performance(game_data)`**: Takes a list of dictionaries containing data from each round. It calculates and prints statistics for each player, including:
    -   Mean and standard deviation of bids.
    -   Final score.
    -   Total wins and win percentage.

## Example Output

Here is an example of the output from a 2-player bot-only game:

```
Players: ['Bot1', 'Bot4']

Starting game...

Card 5 | Bids: {'Bot1': 5, 'Bot4': 1}
Bot1: 5.0
Bot4: 0.0
----------------------------------------
Card 11 | Bids: {'Bot1': 11, 'Bot4': 2}
Bot1: 16.0
Bot4: 0.0
----------------------------------------
...
(Game continues for all 13 cards)
...
----------------------------------------
Card 10 | Bids: {'Bot1': 10, 'Bot4': 13}
Bot1: 55.0
Bot4: 36.0
----------------------------------------

🏆 Winner: Bot1 (Score: 55.0)

📊 Bot1 Performance:
  Bids: μ=7.00, σ=3.89
  Score: 55.00
  Wins: 7/13 (53.8%)

📊 Bot4 Performance:
  Bids: μ=7.00, σ=3.89
  Score: 36.00
  Wins: 6/13 (46.2%)
```
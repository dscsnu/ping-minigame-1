# Blckjack minigame 4 ping 

legal gambling bro 🤘

## Process and Functioning

1. The application loads all strategy files from the `strats` directory.
2. It initializes each strategy with a set amount of credits (default: 1000).
3. The simulation runs for a minimum number of rounds (default: 50) or until the player runs out of credits.
4. For each round:
   - The player places a bet based on their strategy.
   - Cards are dealt to the player and dealer.
   - The player makes decisions (hit, stand, etc.) based on their strategy.
   - The dealer plays according to standard rules (hit on 16 or below, stand on 17 or above).
   - The round result is determined, and credits are adjusted accordingly.
5. After all rounds, the application plots the performance of each strategy and prints the final results.

## Available Classes and Types

1. `Card`: Represents a playing card with a rank and suit.
2. `Deck`: Represents a deck of cards with methods to draw cards.
3. `Player`: Represents a player with credits, a hand, and a strategy.
4. `BlackjackGame`: Manages the game logic for a single round of blackjack.
5. `Strategy`: An abstract base class that all strategies should inherit from.

## Creating a New Strategy

To create a new strategy:

1. Create a new Python file in the `strats` directory (e.g., `my_strategy.py`).
2. Define a `Strategy` class in this file with the following methods:
   - `__init__(self)`: Initialize any strategy-specific variables.
   - `decide_bet(self, player_credits)`: Decide the bet amount for the round.
   - `decide_action(self, player_hand, dealer_up_card)`: Decide the action to take (hit or stand).
   - `decide_split(self, player_hand)`: Decide whether to split a pair (optional).
   - `decide_double_down(self, player_hand)`: Decide whether to double down (optional).
   - `update_result(self, result)`: Update the strategy based on the round result (optional).

Here's a boilerplate code for a new strategy:

// to b added





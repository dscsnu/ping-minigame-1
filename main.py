import os
import importlib
import matplotlib.pyplot as plt
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, initial_credits, strategy):
        self.name = name
        self.credits = initial_credits
        self.strategy = strategy
        self.hand = []
        self.rounds = 0

    def reset_hand(self):
        self.hand = []

class BlackjackGame:
    def __init__(self, player):
        self.player = player
        self.dealer_hand = []

    def play_round(self):
        deck = Deck()
        self.player.reset_hand()
        self.dealer_hand = []

        # Initial deal
        self.player.hand.append(deck.draw())
        self.dealer_hand.append(deck.draw())
        self.player.hand.append(deck.draw())
        self.dealer_hand.append(deck.draw())

        # Player's turn
        bet = self.player.strategy.decide_bet(self.player.credits)
        self.player.credits -= bet

        while True:
            action = self.player.strategy.decide_action(self.player.hand, self.dealer_hand[0])
            if action == 'stand':
                break
            elif action == 'hit':
                self.player.hand.append(deck.draw())
                if self.calculate_hand_value(self.player.hand) > 21:
                    self.player.strategy.update_result('loss')
                    self.player.rounds += 1
                    return  # Player busts

        # Dealer's turn
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(deck.draw())

        # Determine winner
        player_value = self.calculate_hand_value(self.player.hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if dealer_value > 21 or player_value > dealer_value:
            self.player.credits += bet * 2
            self.player.strategy.update_result('win')
        elif player_value < dealer_value:
            self.player.strategy.update_result('loss')
        else:
            self.player.credits += bet  # Push
            self.player.strategy.update_result('push')

        self.player.rounds += 1

    @staticmethod
    def calculate_hand_value(hand):
        value = sum(card.value() for card in hand)
        aces = sum(1 for card in hand if card.rank == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value



def load_strategies():
    strategies = {}
    strats_dir = 'strats'
    for filename in os.listdir(strats_dir):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            module = importlib.import_module(f'{strats_dir}.{module_name}')
            strategy_class = getattr(module, 'Strategy')
            strategies[module_name] = strategy_class()
    return strategies

def simulate_games(strategies, initial_credits=1000, min_rounds=50):
    results = {name: {'credits': [initial_credits], 'rounds': 0} for name in strategies}
    
    for name, strategy in strategies.items():
        player = Player(name, initial_credits, strategy)
        game = BlackjackGame(player)
        
        while player.credits > 0 and player.rounds < min_rounds:
            game.play_round()
            results[name]['credits'].append(player.credits)
            results[name]['rounds'] += 1
    
    return results

def plot_results(results):
    plt.figure(figsize=(12, 6))
    for name, data in results.items():
        plt.plot(range(len(data['credits'])), data['credits'], label=name)
    
    plt.xlabel('Rounds')
    plt.ylabel('Credits')
    plt.title('Blackjack Strategy Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('strategy_performance.png')
    plt.close()


def main():
    strategies = load_strategies()
    results = simulate_games(strategies)
    plot_results(results)
    
    # Print final results
    print("Final Results:")
    for name, data in results.items():
        print(f"{name}: {data['credits'][-1]} credits after {data['rounds']} rounds")

if __name__ == "__main__":
    main()

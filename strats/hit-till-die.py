class Strategy:
    def __init__(self):
        # Set the fixed bet amount to 50 credits
        self.bet_amount = 50

    def decide_bet(self, player_credits):
        """
        Decide the bet amount for this round.
        
        Args:
            player_credits (int): The current amount of credits the player has.
        
        Returns:
            int: The bet amount, which is always 50 in this strategy.
        """
        # Always return the fixed bet amount, regardless of player's credits
        return self.bet_amount

    def decide_action(self, player_hand, dealer_up_card):
        """
        Decide the action to take based on the player's hand and dealer's up card.
        
        Args:
            player_hand (list): The player's current hand.
            dealer_up_card (Card): The dealer's face-up card.
        
        Returns:
            str: The action to take, which is always 'hit' in this strategy.
        """
        # This strategy always chooses to hit, regardless of the player's hand or dealer's up card
        return 'hit'

    def decide_split(self, player_hand):
        """
        Decide whether to split a pair.
        
        Args:
            player_hand (list): The player's current hand.
        
        Returns:
            bool: Always False in this strategy, as we never split.
        """
        # This strategy never splits, so always return False
        return False

    def decide_double_down(self, player_hand):
        """
        Decide whether to double down.
        
        Args:
            player_hand (list): The player's current hand.
        
        Returns:
            bool: Always False in this strategy, as we never double down.
        """
        # This strategy never doubles down, so always return False
        return False

    def update_result(self, result):
        """
        Update the strategy based on the result of the last hand.
        
        Args:
            result (str): The result of the last hand ('win', 'loss', or 'push').
        """
        # This strategy doesn't change its behavior based on results,
        # but we implement this method to be compatible with the game logic
        pass
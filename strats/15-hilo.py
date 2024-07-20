class Strategy:
    def __init__(self):
        self.base_bet = 50
        self.current_bet = self.base_bet
        self.last_result = None

    def decide_bet(self, player_credits):
        if self.last_result == 'loss':
            self.current_bet *= 2
        elif self.last_result == 'win' or self.last_result is None:
            self.current_bet = self.base_bet
        
        return min(self.current_bet, player_credits)

    def decide_action(self, player_hand, dealer_up_card):
        hand_value = self.calculate_hand_value(player_hand)
        
        if hand_value < 15:
            return 'hit'
        else:
            return 'stand'

    def decide_split(self, player_hand):
        return False

    def decide_double_down(self, player_hand):
        return False

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                aces += 1
            else:
                value += int(card.rank)
        
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        
        return value

    def update_result(self, result):
        """
        Update the last result to adjust the next bet.
        
        Args:
            result (str): 'win', 'loss', or 'push' indicating the result of the last round.
        """
        self.last_result = result
import random
player = []
dealer = []

class Card:
    def __init__(self, total) -> None:
        self.total = total
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def sum(self):
        if self.total >= 10:
            return 10
        elif self.total == 1:
            return 11
        return self.total
    
class Deck:
    def __init__(self) -> None:
        self.card = []

        for i in range(1, 14):
            self.card.append(Card(i))
            return self.card

    def deal_card(self):
        cards = []
        the_card = random.choice(self.card)
        cards.append(the_card)
        self.card.remove(the_card)
    
    def count(self):
        return len(self.card)

class Player(Deck):
    def __init__(self, player, dealer) -> None:
        self.card = []
        self.sum = 0
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
        
    def winner(self):
        ace = 0
        self.sum = 0
        for card in self.card:
            if card.sum() == 11:
                ace += 1
            self.sum += card.sum()

    def reveal_play(self):
        if len(self.dealer) == 2:
            return self.dealer[0]
        elif len(self.dealer) > 2:
            return self.dealer[0], self.dealer[1]

        for _ in range(2):
            self.deck.deal_card(self.dealer)
            self.deck.deal_card(self.player)

    while player is True and dealer is True:
        print(f"Dealer has {reveal_play()}")
        print(f"You have {player} for a total of {sum(player)}")
# to be continued ...


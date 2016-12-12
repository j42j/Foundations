"""Play a round of blackjack against the dealer"""
import random
import itertools

class Card():
    """put doc here"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return str(self.rank) + self.suit

    def get_points(self):
        if (1 < self.rank <= 10):
            return [self.rank]
        elif (self.rank > 10):
            return [10]

        return [1, 11]

class Hand():
    def __init__(self, c1, c2):
        self.cards = []
        self.add_card(c1)
        self.add_card(c2)

    def add_card(self, c):
        self.cards.append(c)

    def get_points(self):
        points = [0]
        for c in self.cards:
            cp = c.get_points()
            points = [x + y for x, y in itertools.product(points, cp)]

        points.sort()
        best = points.pop()

        for p in points:
            if p <= 21:
                best = p
        return best

    def __repr__(self):
        return repr(self.cards)

ranks = range(1, 14)
suits = ('H', 'S', 'D', 'C')
deck = []
for suit, rank in itertools.product(suits, ranks):
    deck.append(Card(suit, rank))

def get_shuffled_deck():
    d = deck[:]
    random.shuffle(d)
    return d

def main():
    while True:
        ans = input('Do you want to start a Blackjack game? (y/n):  ')
        cleaned = ans.strip().lower()
        if cleaned in ('n', 'no'):
            break
        elif cleaned not in ('y', 'yes'):
            print('Invalid response.')
            continue

        game_deck = get_shuffled_deck()

        p_hand = Hand(game_deck.pop(), game_deck.pop())
        d_hand = Hand(game_deck.pop(), game_deck.pop())

        print("The dealer's face-up card is ", d_hand.cards[0])
        p_points = p_hand.get_points()
        d_points = d_hand.get_points()

        # if p_points == 21:
        #     print("Your hand is ", p_hand)
        #     if d_points != 21:
        #         print("You win!")
        #     else:
        #         print("You tie!")
        #     break


        while p_points < 21:
            print("Your hand is ", p_hand)

            a2 = input('Do you want to hit? (y/n):  ')
            if a2 == 'n':
                break
            elif a2 == 'y':
                c = game_deck.pop()
                p_hand.add_card(c)
                p_points = p_hand.get_points()
                print("You drew ", c)

        if p_points > 21:
            print("You went bust! You lose.")

if __name__ == "__main__":
main()

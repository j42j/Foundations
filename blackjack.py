"""Play multiple rounds of blackjack against the dealer"""
import random
import itertools

class Card():
    """Cards class has attributes suit (H,S,C,D)
    and rank (1-13) where 11, 12, 13 is J, Q, K"""

    ranks = range(1, 14)
    suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_pretty_rank(self):
        pretty_rank = {x: y for x, y in zip(list(self.ranks),
                       ["Ace", *list(range(2,11)), "Jack", "Queen", "King"])}
        return str(pretty_rank[self.rank])

    def __repr__(self):
        return self.get_pretty_rank() +  ' of ' + self.suit

    def get_points(self):
        """If card has rank 2-10, return rank
        If card is J, Q, or K, return 10
        If card is Ace, return 1 and 11 (list)"""

        if 1 < self.rank <= 10:
            return [self.rank]
        elif (self.rank > 10):
            return [10]

        return [1, 11]


class Deck(Card):
    """Deck class extends Card"""

    def __init__(self):
        self.deck = []
        for c_suit, c_rank in itertools.product(Card.suits, Card.ranks):
            self.deck.append(Card(c_suit, c_rank))

    def get_shuffled_deck(self):
        random.shuffle(self.deck)
        return self.deck


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
            points = [x + y for x, y in itertools.product(points,  cp)]

        points.sort()
        best = points.pop()

        for p in points:
            if p <= 21:
                best = p
        return best

    def __repr__(self):
        return repr(self.cards)


def main():
    while True:
        ans = input('Do you want to start a Blackjack game? (y/n):  ')
        if ans == 'n':
            break
        elif ans != 'y':
            print('Invalid response.')
            continue

        game_deck = Deck().get_shuffled_deck()
        p_hand = Hand(game_deck.pop(), game_deck.pop())
        d_hand = Hand(game_deck.pop(), game_deck.pop())

        print("The dealer's face-up card is ", d_hand.cards[0])
        print("Your hand is ", p_hand)
        p_points = p_hand.get_points()
        d_points = d_hand.get_points()

        # Check for naturals
        if p_points == 21:
            print('The dealer\'s hand is ', d_hand)
            if d_points != 21:
                print('You have Blackjack! You win!')
            else:
                print('You tie!')
        else:
            if d_points == 21:
                print('You lose!')

        #play hand of blackjack until bust or stand
        while p_points < 21 and d_points != 21:
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
        elif p_points == 21:
            print("The dealer's hidden card is ", d_hand.cards[1])
            print("The dealer's hand is ", d_hand)
            print("You have Blackjack! You win!")
        else:
            print("The dealer's hidden card is ", d_hand.cards[1])
            print("The dealer's hand is ", d_hand)
            print("The dealer will play.")
            while d_points < 17:
                c = game_deck.pop()
                d_hand.add_card(c)
                d_points = d_hand.get_points()
            print("The dealer's final hand is ", d_hand)
            if d_points > 21 or p_points > d_points:
                print("You win!")
            elif p_points < d_points:
                print("You lose!")
            else:
                print("You tie!")

if __name__ == "__main__":
    main()

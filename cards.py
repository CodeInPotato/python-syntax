import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck contains: ' + deck_comp

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if self.cards == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Please provide a number.")
        else:
            if chips.bet > chips.total:
                print(f'Sorry number exceeded the amount of chips that you carry. You have {chips.total} chips.')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h/s')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player STANDS, Dealer's Turn")
            playing = False
        else:
            print("Wrong input. Hit or Stand? Enter h/s")
            continue

        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer_hand.cards[1])
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer_hand.cards, sep='\n ')
    print("Dealer's Hand =", dealer_hand.value)
    print("\nPlayer's Hand:", *player_hand.cards, sep='\n ')
    print("Player's Hand =", player_hand.value)


def player_busts(player, dealer, chips):
    print("Player BUSTS")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player WINS, Dealer BUSTS")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer WINS")


def push(player, dealer):
    print("Dealer and Player TIES! PUSH!")


while True:
    playing = True
    print('Welcome!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    for x in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f'You now have {player_chips.total} chips!')

    new_game = input(print('\n Would you like to play another Hand? y/n'))
    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break
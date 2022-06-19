# used shuffle method from random module as well as time

from random import shuffle
import time

suits = ('Hearts - ♥', 'Diamonds - ♦', 'Spades - ♠', 'Clubs - ♣')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:
    
    def __init__(self,suit,rank): # parameters needed to instantiate the card class are suit and rank
        self.suit = suit
        self.rank = rank
        
    def __str__(self): # the __str__() method allows us to print when we call the card class instead of just a memory location
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list to which will append cards using the loops
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(): # __str__() method to return the entire deck of cards
        deck_compostion = ''
        
        for card in self.deck:
            deck_composition += '\n'+ card.__str__()
        return 'The deck has: ' + deck_composition

    def shuffle(self):
        shuffle(self.deck)
        
    def deal_one(self): # method to deal a card, this can be called multiple times - pop() method takes a card from very top of the deck
        one_card = self.deck.pop()
        return one_card


class Hand:
    
    def __init__(self):  # instantiate the class with the following:
        self.cards = []  # empty list as we did in the Deck class
        self.value = 0   # value of 0
        self.aces = 0    # attribute to keep track of aces
    
    def add_card(self,new_card): # takes in new_card parameter which will be deal_one() method from deck class
        self.cards.append(new_card)
        self.value += values[new_card.rank] # values method used to grab value of said card from the dictionary
        
        if new_card.rank == "Ace":
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0: # can also just say self.aces as a value of an integer larger than zero is TRUE
            self.value -= 10 # while we have a total value > 21, and a ace we can reduce the value by 10 as ace can be 11 or 1
            self.aces -= 10


class Chips:
    
    def __init__(self):
        self.total_chips = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0 # this is the bet the player wants to make and will be assigned a value from the take_bet() method
        
    def win_bet(self):
        self.total_chips += self.bet # if game is won, bet is added onto total chips
    
    def lose_bet(self):
        self.total_chips -= self.bet # if game is lost, bet is removed from total chips


def take_bet(chips): # will ask the player to place a bet and add it to self.bet variable in Chips class
    
    while True:
        try:
            chips.bet = int(input("\nEnter the amount of chips you'd like to bet: "))
        except:
            print("\nThat's not a number, please try again...") # used try and except to counter error resulting from str input
        else:
            if chips.bet > chips.total_chips: # need to ensure the bet does not exceed the total amount of chips a player holds
                print(f"\nSorry, you dont have enough chips and your bet cannot exceed: {chips.total_chips}.")
            else:
                break

def hit(deck,hand): 
    # called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17
    # Deck and Hand objects arguments, and deal one card off the deck and add it to the Hand
    # also want to adjust for the ace if needed
    
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def stay_or_draw(deck,hand):
    # If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False
    # this will control the behavior of a while loop later on in our code
    
    global playing # can be at very start of this giant code blocc
    
    while True:
        choice = input("\nWould you like to Stay with your current hand or Draw a card? (S/D): ")

        if choice[0].lower() == "s":
            print("\nThe player has chosen to stay, the dealer is now playing.")
            time.sleep(2)
            playing = False # as player has chosen to stay

        elif choice[0].lower() == "d":
            print("\nDrawing a card...")
            time.sleep(1.5)
            hit(deck,hand)

        else:
            print("\nSorry, please enter \"Stay\" or \"Draw\"") # use of \ to nullify the string ending
            continue
        break


def semi_reveal(player_hand,dealer_hand):
    
    
    # so we will name the Hand() class with respect to the two arguments passed into the semi_reveal function
    
    # so initially, we only want to show one of the dealers cards
    print("\nDealer's Hand: ")
    print("\t<< Hidden card >>")
    print("\t", (dealer_hand.cards[1]))
    
    # and we also show the players card but instead show all of them
    print("\nPlayer's Hand: ")
    for card in player_hand.cards:
        print("\t", (card))
    print(f"\nThe current value of the player's hand is {player_hand.value}")
    
def full_reveal(player_hand,dealer_hand):
          
    # so initially, we only want to show one of the dealers cards
    print("\nDealer's Hand: ")
    for card in dealer_hand.cards:
        print("\t", (card))
    print(f"\nThe value of the Dealer's hand is {dealer_hand.value}")
    
    # and we also show the players card but instead show all of them
    print("\nPlayer's hand: ")
    for card in player_hand.cards:
        print("\t", (card))
    print(f"\nThe value of the Player's hand is {player_hand.value}")


# so now we will configure a series of functions to handle end of game scenarios

def player_busts(chips):
    print("\nPlayer has bust! Dealer wins")
    chips.lose_bet()
    
def dealer_wins(chips):
    print("\nDealer has won!")
    chips.lose_bet()

def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("\nDealer has bust! Player wins")
    chips.win_bet()

def tie():
    print("\nThe Dealer got the same score! The game is a draw")


# so now to run the game



# set up the players chips, done outside the while loops so that the 100 chips are are instantiated once and not reset each loop

player_chips = Chips()

# opening statement
    
print("\nWelcome to the original Blackjack™ game")
print("\nTry to get as close to a value of 21 as you can by either choosing to draw a card or stay put.")
print('''Face cards have a value of 10 and Aces can be worth either 11 or 1, and their value will adjust to 
give you the best possible score.''')
print("This game can run infinitely so lets set a goal of 250 chips :)")
print("Your initial Chip set is 100")
print("\nHave fun!")

while True:
    # instantiate (create) and shuffle the deck
    
    game_deck = Deck()
    game_deck.shuffle()
    
    # set up the player and dealer hands and then deal two cards to them
    
    player_hand = Hand()
    player_hand.add_card(game_deck.deal_one())
    player_hand.add_card(game_deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal_one())
    dealer_hand.add_card(game_deck.deal_one())
    
    
    # prompt the player for their bet & pace the game
    
    take_bet(player_chips)
    print("\nInitialising deck & chip set and shuffling & dealing cards...")
    time.sleep(3)
    
    # so, initially, before asking to draw or stay we want to show the player the cards (one dealer card is missing)
    
    semi_reveal(player_hand, dealer_hand)
    
    playing = True
    
    while playing: # this is assigned "True" as a global variable in the stay_or_draw function
        
        # prompt the player to stay or draw a card
        
        stay_or_draw(game_deck, player_hand)
        
        # show the cards (keeping one dealer card hidden)
        
        semi_reveal(player_hand, dealer_hand)
        
        # if the players hand busts, exceeding 21, run the busts() sequence and break out of the loop
        
        if player_hand.value > 21:
            
            player_busts(player_chips)
            break
            
    # if the player doesn't bust, play the dealers hand until it reaches 17
    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            
            hit(game_deck, dealer_hand)
            
        # show all the cards
        
        full_reveal(player_hand, dealer_hand)
        
        # then run the different winning scenarios
        
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
            
        elif player_hand.value > 21:
            player_busts(player_chips)
            
        elif player_hand.value > dealer_hand.value:
            player_wins(player_chips)
            
        else:
            tie()
    
    # show the standing of the players current chips total
    
    print("\nThe player currently has {} chips".format(player_chips.total_chips))
    
    if player_chips.total_chips == 0:
        print("\nSorry mate, ya have no chips left to play the game with, lucky for you, you're able to run the script again")
        break
    elif player_chips.total_chips >= 250:
        print("\nCongrats dude, you absolutely dominated and hold a whopping {} chips!!!".format(player_chips.total_chips))
        break
    else:
    # ask to play again

        replay = input("\nWould you like to play again (Y/N) ")

        if replay[0].lower() == "y":
            playing = True
            continue
        else:
            print("\nThanks for playing <3")
            break

# :)



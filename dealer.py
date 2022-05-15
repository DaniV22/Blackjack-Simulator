from clear import clear
from time import sleep
from cards import Card, Deck

class Dealer:

    '''
    Create the Dealer class (similar to Player class)

    ATTRIBUTES:

        all_cards : the cards in the hand(s) of the player
		name : name of the player
        hand_value : the total value of the hand(s)
        bust : a boolean to know if player busted

	METHOD:

        add_card :       adds a new card to Dealer hand
        hand :           counts the total value of the player hand
        show_cards :     shows the cards in Dealer hand (it can hide one card)

    '''
    
    def __init__(self):
        
        self.all_cards = []
        self.name = 'Dealer'
        self.hand_value = 0
        self.bust = False
    
    def add_card(self, new_cards):
        
        self.all_cards.append(new_cards)

    def hand(self):
        
        aces = 0
        self.hand_value = 0
        
        #Sum of the values of the cards
        for cards in self.all_cards:
            self.hand_value += cards.value
            
            #Counting the number of Aces and adjusting the hand value when needed
            if cards.rank == 'Ace':
                aces += 1
            
            if (self.hand_value > 21) and (aces >=1):
                self.hand_value -= aces*10
                aces = 0
        return self.hand_value

    def show_cards(self, show_all = False):

        #Displaying Dealer's cards. During the game, one is hidden

        print("Dealer's cards: \n")
        sleep(2)
        
        #Showing all cards
        if show_all == True:
            for cards in self.all_cards:
                print(cards)
            print('')
            
        #Hiding the card in position [0]
        else: 
            print('Hidden card')
            for x in range(1, len(self.all_cards)):
                print(self.all_cards[x])
            print('')
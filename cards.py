import random

#Tupple of suits and ranks in Blackjack
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five','Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack','Queen', 'King', 'Ace')

#A dictionary with the values of cards (Blackjack)
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

	'''
	A class that creates a card object

	ATTRIBUTES:

		suit : 		the suit of the card
		rank : 		the rank of the card
		value : 	the value of the card (according to Blackjack rules)

	METHOD:

		str : 	returns the name of the card
	'''

	def __init__(self, suit, rank):

		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):

		return self.rank + " of " + self.suit


class Deck:

	'''
	Creates a Deck object using the Card class

	ATTRIBUTES:

		all_cards : 	a list containing every card in the Deck

	METHOD:

		shuffle : 		shuffles the deck of cards
		deal_card : 	returns the last card in the deck
	'''
    
    #We play a single-deck game
	def __init__(self):

		self.all_cards = []

		#Creating every possible card in the game
		for suit in suits:
			for rank in ranks:
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)
        
	def shuffle(self):

		random.shuffle(self.all_cards)

	def deal_card(self):

		return self.all_cards.pop()



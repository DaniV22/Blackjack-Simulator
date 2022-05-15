from clear import clear
from time import sleep
from cards import Card, Deck

class Player:


    '''
	Creates the Player class

	ATTRIBUTES:

		name : name of the player
        chips : current chips of the player
        all_cards : the cards in the hand(s) of the player
        hand_value : the total value of the hand(s)
        bet : the bet provided by the player
        bust : a boolean to know if player busted (single-hand game)
        hand_bust : a list of booleans (splitting pairs)

	METHOD:

		str : 		     returns the name and the current chips of the player
        len :            returns the number of hands
        win_lose_bet :   adds (takes) the bet from chips when player wins (loses)
        add_card :       adds a new card to player hand
        hand :           counts the total value of the player hand
        show_cards :     shows the cards in player hand
        make_bet :       used at the beginning of every round to make a bet
        double_down :    doubles the bet of the player
        remove_bet :     removes the player bet

    '''

    def __init__(self, name, chips):

        self.name = name
        self.chips = chips
        self.all_cards = [[],[]] #No cards by default and up to two hands (Splitting Pairs)
        self.hand_value = [0,0]
        self.bet = [0,0]
        self.bust = False #Used in single-hand game
        self.hand_bust = [False, False] #Used when Splitting Pairs

    def __str__(self):
            return f"Player:   {self.name} \n Chips:   ${self.chips}"

    #Number of hands
    def __len__(self):
        num_hands = [hand for hand in self.all_cards if len(hand) > 0] #A hand of length 0 it's NOT a hand
        return len(num_hands)

    def win_lose_bet(self, bet):

        #When Player win/lose, the bet is added/taken from Player's chips
        #Since 'negative bets' are used, the bet is always added to Player's chips
        self.chips += bet
        
        if bet > 0:
            print('You have won ' + str(bet) + ' chips! You have ' + str(self.chips) + ' now!')
        
        else:
            print('You have lost ' + str(-bet) + ' chips! You have ' + str(self.chips) + ' now!')
            
    def add_card(self, new_cards, num_hand=0):
        
        self.all_cards[num_hand].append(new_cards)
            
    def hand(self):

        aces = [0,0]

        #Sum of the values of the cards
        for i in range(len(self)):
            
            total_value = 0

            for cards in self.all_cards[i]:
                total_value += cards.value

                #Counting the number of Aces and adjusting the hand value when needed
                if cards.rank == 'Ace':
                    aces[i] += 1

                if (total_value > 21)and(aces[i] >= 1):
                    total_value -= 10
                    aces[i] -= 1
            
            self.hand_value[i] = total_value
        
        return self.hand_value
    
    def show_cards(self, num_hand=0):

        #Displaying all Player's card depending on the hand's number
    
        #Single hand
        if len(self) == 1:
            print(f"{self.name}'s cards: \n")
            sleep(2)

            for cards in self.all_cards[0]:
                print(cards)
            print('\n')
            
        #Double hand (Splitting Pairs)
        else:
            if num_hand == 0:
                print(f"{self.name}'s left-hand cards: \n")
                sleep(2)
                
                for cards in self.all_cards[0]:
                    print(cards)
                print('\n')
                
            else:
                print(f"{self.name}'s right-hand cards: \n")
                sleep(2)
                
                for cards in self.all_cards[1]:
                    print(cards)
                print('\n')
        
    def make_bet(self):

        while self.bet[0] == 0:
            try:
                print(f"Current balance: {self.chips}.")
                bet_on_hand = int(input(f'{self.name}, choose your bet: '))

            except ValueError:
                print('Please, provide an integer number')
                sleep(2)
                continue
            else:
                if bet_on_hand not in range(0, self.chips+1):
                    print('Please, provide a posible quantity')
                else:
                    self.bet = [bet_on_hand, 0] #By default, there's no bet in the second hand
                    break
        
        clear()
    
    def double_down(self, hand_number):
        
        self.bet[0] = 2*self.bet[0]
                
        print(f"Double Down! {self.name}'s bet is now " + str(self.bet[0]))
        sleep(2)
                
        print(f'{self.name} takes another card')
        print('')
    
    def remove_bet(self, hand_number):
        
        self.bet[hand_number] = 0   


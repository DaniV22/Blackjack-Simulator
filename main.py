from time import sleep
from clear import clear
from cards import Deck
from player import Player
from dealer import Dealer



def main():

    print('WELCOME TO BLACKJACK SIMULATOR. GOOD LUCK!\n')
    sleep(2)

    player_name = input('Please, choose your name: ')

    #Choosing initial chips (a positive integer number)         
    while True:

        try:
            init_chips = int(input(f'{player_name}, choose your initial chips: '))
                
        except:
            print('Please, provide a positive integer number')
            continue
                
        else:
            if init_chips <= 0:
                print('Please, provide a positive integer number')
                    
            else:
                break

    clear()

    while True:
        
        #GAMEPLAY SETUP
        
        player = Player(player_name, init_chips)
        dealer = Dealer()
        player.make_bet()
        
        sleep(1)
        clear()
        
        #Some default variable
        player_blackjack = False
        dealer_blackjack = False
        dealer_is_playing = True
        playing = True
        game_turn = 1
        hand_number = 0
        
        #Creating and shuffling the deck and dealing two cards each player
        new_deck = Deck()
        new_deck.shuffle()
        
        for x in range(2):
            player.add_card(new_deck.deal_card())
            dealer.add_card(new_deck.deal_card())
        
        print('GAME STARTING SOON')
        sleep(1)
        clear()
        print('GAME STARTING SOON .')
        sleep(1)
        clear()
        print('GAME STARTING SOON . .')
        sleep(1)
        clear()
        print('GAME STARTING SOON . . .')
        sleep(1)
        clear()
        
        #Showing the Player and Dealer's cards (one hidden)
        player.show_cards()
        sleep(3)
        dealer.show_cards(False)
        sleep(3)
        clear()
        
        #Checking if there's a Blackjack. If so, player and dealer don't play
        if player.hand()[0] == 21:
            print(f'{player.name} has a BLACKJACK!')
            player_blackjack = True
            dealer_is_playing = False
            playing = False
        
        elif dealer.hand() == 21:
            print('Dealer has a BLACKJACK!')
            dealer_blackjack = True
            dealer_is_playing = False
            playing = False
        
        else:
            print("Player's turn \n")
            sleep(2)

        #Iterating through player's hands (one by default)
        while hand_number in range(0,len(player)):
            
            if hand_number == 1:
                print(f'Right-hand turn: {player.name} takes another card')
                player.add_card(new_deck.deal_card(), hand_number)
                sleep(3)
                clear()
                player.show_cards(hand_number)
                sleep(3)
        
            while playing:
                
                #Asking the user for his/her choice
                choice = 'vfhsghg'  #Dummy value
                choices = ['H', 'HIT', 'hit', 'h', 'STAND', 'stand', 'S', 's']
                text = 'Choose to Hit (H) or to Stand (S): '
                
                if game_turn == 1 and player.bet[0]*2 <= player.chips:
                    choices.extend(['DD', 'dd'])
                    text = 'Choose to Hit (H), to Stand (S) or to Double Down (DD): '
                
                    #Since SPLIT requieres an additional bet, player needs, at least, 2*bet chips
                    if player.all_cards[0][0].value == player.all_cards[0][1].value:
                        choices.extend(['split', 'SPLIT', 'SP', 'sp'])
                        text = 'Choose to Hit (H), to Stand (S), to Double Down (DD) or to Split Pairs(SP): '
                
                while choice not in choices:
                    choice = input(text)
        
                    if choice not in choices:
                        print('Please, choose a valid answer: ')
                
                sleep(2)
                clear()
                        
                #Executing the function associated with the choice
                if choice in ['H', 'HIT', 'hit', 'h']:
                    
                    print(f'{player.name} takes another card')
                    print('')
                    player.add_card(new_deck.deal_card(), hand_number)
                    player.show_cards(hand_number)
        
                elif choice in ['DD', 'dd']:
                    
                    player.double_down(hand_number)
                    player.add_card(new_deck.deal_card(), hand_number)
                    player.show_cards(hand_number)
                    playing = False
                    
                elif choice in ['STAND', 'stand', 'S', 's']:
                    playing = False
                    print(f"{player.name} stands at {player.hand()[hand_number]} points")
                    sleep(2)
                    clear()
                    pass
        
                else:       #Split case  
                    print(f"{player.name} has decided to Split Pairs! \n")
                    new_card = player.all_cards[0].pop()
                    player.add_card(new_card, num_hand=1)
                    player.bet[1] = player.bet[0] #An additional bet is made
                    
                    sleep(2)
                    print(f'{player.name} takes another card \n')
                    player.add_card(new_deck.deal_card(), hand_number)
                    
                    sleep(2)
                    clear()
                    
                    player.show_cards(hand_number)
                    sleep(2)
                    
                game_turn += 1           
                
                #Checking if player bust
                if len(player) == 1:
                    if player.hand()[hand_number] > 21:
                        sleep(3)
                        clear()
                        print(f'{player.name} BUST! Your hand has exceeded 21 points! \n')
                        sleep(1)
                        
                        player.win_lose_bet(-player.bet[0])
                        player.bust = True
                        playing = False
                
                elif len(player) ==2: 
                    if player.hand()[hand_number] > 21:
                        sleep(2)
                        clear()
                        print(f"{player.name}'s " + str(hand_number+1) + 
                            " hand BUST! Your hand has exceeded 21 points!")
                        sleep(3)
                        
                        playing = False
                        player.win_lose_bet(-player.bet[hand_number])
                        player.hand_bust[hand_number] = True
                        player.remove_bet(hand_number)
                        
                    
            hand_number += 1
            playing =  True
        
        sleep(2)
        clear()
            
        #Checking whether the Dealer has to play or not
            
        #If the value of the Dealer's hand is already greater (or equal)
        #than 17 he will not play    
        # If anyone got a Blackjack, Dealer will not play
        # If player bust (both hands) Dealer will not play
        
        if [player.hand_bust[0], player.hand_bust[1]] == [True, True]:
            dealer_is_playing = False
            
        elif player.bust == True:
            dealer_is_playing = False
            
        elif dealer_is_playing == False: #Blackjack case
            pass
        
        else:
            if dealer.hand()<17:
                dealer_is_playing = True
                print("Dealer's turn \n")
                sleep(3)
            else:
                print(f'Dealer stands at {dealer.hand()} points \n')
                sleep(3)
                clear()
                dealer_is_playing = False
                dealer.show_cards(True) #Showing all cards

        #Dealer turn   
        while dealer_is_playing:
            
            print('Dealer takes another card \n')
            dealer.add_card(new_deck.deal_card())

            sleep(2)
            clear()

            dealer.show_cards(True)
            sleep(3)

            if dealer.hand()<17:
                pass

            elif dealer.hand()>21:
                clear()
                print('Dealer BUST! His hand has exceeded 21 points! \n')
                sleep(3)
                dealer.bust = True
                player.win_lose_bet(sum(player.bet)) #Using sum to consider the (possible) two hands case
                dealer_is_playing = False
            else:
                clear()
                print(f'Dealer stands at {dealer.hand()} points \n')
                sleep(1)
                dealer_is_playing = False
            
        sleep(2)

        #Checking the different endings
        if player_blackjack == True or dealer_blackjack == True:
            
            if player_blackjack and dealer_blackjack:
                print('STAND-OFF! Both have a Blackjack!\n')
                print(f"{player.name}'s bet is returned")
            elif player_blackjack:
                if player.bet[0] % 2 == 0:
                    player.win_lose_bet(int(1.5*player.bet[0]))
                else:
                    player.win_lose_bet(int(1.5*player.bet[0]-0.5)) #Rounded down
                    
            else:     
                player.win_lose_bet(-player.bet[0])
        
        elif dealer.bust == True or player.bust == True:
            
            #The bust cases have been already checked
            pass
        
        #Player hand(s) vs Dealer hand
        else:  
            for hand_number in range(len(player)):
                
                if player.hand_bust[hand_number] == True:
                    pass
                
                else:
                    if player.hand()[hand_number] > dealer.hand():
                        
                        if len(player) == 2:
                            print(f'{player.name} wins the Dealer with the hand {hand_number}!\n ')
                            sleep(2)
                        elif len(player) == 1:
                            print(f'{player.name} wins the Dealer!\n')
                            sleep(2)
                            
                        player.win_lose_bet(player.bet[hand_number])
                    
                    elif player.hand()[hand_number] < dealer.hand():
                        
                        if len(player) == 2:
                            print(f'{player.name} loses against the Dealer with the hand {hand_number}!\n ')
                            sleep(2)
                        elif len(player) == 1:
                            print(f'{player.name} loses against the Dealer!\n ')
                            sleep(2)
                            
                        player.win_lose_bet((-player.bet[hand_number]))
                    
                    else:
                        print(f"PUSH! {player.name}'s bet is returned")
                        sleep(2)
        
        #The initial chips of the next round are the remaining ones of this round
        init_chips = player.chips
        if init_chips == 0:
            print("Out of chips. You can't keep playing")
            sleep(3)
            break
                
        
        sleep(2)
        clear()

        play = 'Wrong' #Dummy value

        while play not in ['Y', 'y', 'yes', 'YES', 'N', 'n', 'NO', 'no']:
            play = input('Do you want to keep playing, Yes (Y) or No (N): ')

            if play not in ['Y', 'y', 'yes', 'YES', 'N', 'n', 'NO', 'no']:
                print('Please, choose a valid answer: ')

        if play in ['Y', 'y', 'yes', 'YES']:
            sleep(1)
            clear()
            print('Next Round!')
            sleep(2)
            clear()
        else:
            break
            
    clear()

    print('\n')
    print('THANKS FOR PLAYING BLACKJACK')


if __name__ == '__main__':
    main()


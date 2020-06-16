import os
os.listdir()
### We see that we have 4 files in our folder
# from <bj_classes> we call the 3 classes: Card, Deck, and Player
# from <players> we call the function 'players_bj', used for creating the list with our 4 players
# from <ParticipantsList.txt> we take the attributes of our 4 players
# <bj_game> is the current file


### Import the <random> module, which will be used by both class methods and other functions
import random

from bj_classes import Card
from bj_classes import Deck
from bj_classes import Player

from players import players_bj

### It's created a list with the four players by calling the function <players_bj>
# This variable will be used inside the <blackjack> function
### With <random.choice()> the human player will be randomly assigned one of the 4 players
# from the list <players_list> 
players_list = players_bj()


### It's created the funtion <blackjack> that contains the game (and it's logic)
def blackjack():

    global players_list
    
    playerBJ = random.choice(players_list)
    print("You've been assigned the player: ",
            str(playerBJ.lname) + " " + str(playerBJ.fname) + ", from " + str(playerBJ.nationality) +
          ", born in " + str(playerBJ.dofbirth),
            str(playerBJ.fname) + " has " + str(playerBJ.chips) + " chips",
            "--------------------", " ",
            sep="\n")
    
    
    
    dealer = Player("Dealer", "Jesus", "1975", "Mexico", 0)
    print("You're playin' against dealer " + str(dealer.fname) + 
    ", from " + str(dealer.nationality) + ", born in " + str(dealer.dofbirth),
    "--------------------", " ", sep="\n")

    chips = playerBJ.chips
   
    while chips > 0:
        print("You have a total of " + str(chips) + " chips " + ' \U0001F4B0')
        print("--------------------", " ", sep="\n")
        try:
            betBJ = int(input("How many chips would you like to bet? "))

        except ValueError:
            print('\u2716' + ' Please enter an integer ' + '\u2716')
            continue
            

        if (betBJ > playerBJ.chips and betBJ >= 0) or betBJ == 0:
            print("You cannot bet more than " + str(chips) + " or nothing.")
            continue

        deck = Deck()
        deck.shuffle_deck()

        playerBJ.hand.clear()
        dealer.hand.clear()
        playerBJ.card_sum = 0
        dealer.card_sum = 0
        playerBJ.A = 0
        dealer.A = 0

        playerBJ.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        playerBJ.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

        print("Dealer has in his hand: " + str(dealer.hand[0]))
        print("You, " + str(playerBJ.fname) + ", have in hand: " + str(playerBJ.hand) + 
        " Hand value: " + str(playerBJ.card_sum))
        print("--------------------", " ", sep="\n")

        if dealer.card_sum == 21:
            print("Dealer has BlackJack! " + str(dealer.hand) + " You lost " + '\u2639')
            print("--------------------", " ", sep="\n")
            playerBJ.subtract_chips(betBJ)
            chips -= betBJ
            dealer.A = 0
            continue

        if playerBJ.card_sum == 21:
            print(str(playerBJ.fname) + ", you have BlackJack!" + str(playerBJ.hand) + 
            "You won " + '\U0001F37E' + '\U0001F37E' + '\U0001F37E')
            print("--------------------", " ", sep="\n")
            playerBJ.add_chips(betBJ)
            chips += betBJ
            playerBJ.A = 0
            continue


        while True:
            if playerBJ.card_sum == 21:
                print(str(playerBJ.fname) + ", you have BlackJack!" + str(playerBJ.hand) + 
                " You won " + '\U0001F37E' + '\U0001F37E' + '\U0001F37E')
                
                print("--------------------", " ", sep="\n")
                playerBJ.add_chips(betBJ)
                chips += betBJ
                playerBJ.A = 0
                break
                
                
            hit = input("Would you like to continue or stay? Type: 'C' for another card; 'S' to stay ")
            if hit == ("c" or "C"):
                playerBJ.add_card(deck.deal_card())
                print("You drew: " + "[" + str(playerBJ.hand[-1]) +"]" + " Hand value: " +
                      str(playerBJ.card_sum))
                print("--------------------", " ", sep="\n")

                if playerBJ.card_sum > 21:
                    print("Your hand " +str(playerBJ.hand) + " has a value of: " + str(playerBJ.card_sum) + 
                    ". You lost " + '\u2639')
                    print("--------------------", " ", sep="\n")
                    playerBJ.subtract_chips(betBJ)
                    chips -= betBJ
                    break
                continue
            elif hit == ("s" or "S"):
                break
            else:
                print('\u2716' + ' You have pressed a wrong key ' + '\u2716')
                continue
            
        if playerBJ.card_sum < 21:
            while True:
                print("Dealer has in his in hand: " + str(dealer.hand) + 
                ". Score: " + str(dealer.card_sum))
                print("--------------------", " ", sep="\n")    
                if dealer.card_sum == 21:
                    print("Dealer has Blackjack! You lost " + '\u2639')
                    print("--------------------", " ", sep="\n")
                    playerBJ.subtract_chips(betBJ)
                    chips -= betBJ
                    break

                if playerBJ.card_sum == dealer.card_sum:
                    print ("The value of dealer's hand is " + str (dealer.card_sum) + " " + str (
                        dealer.hand))
                    print (
                        "The value of your hand is " + str (playerBJ.card_sum) + " " + str (playerBJ.hand))
                    print ("Hand ended with a tie")
                    print ("--------------------", " ", sep="\n")
                    break
                    
                while dealer.card_sum < playerBJ.card_sum:

                    if dealer.card_sum < 17:
                        dealer.add_card(deck.deal_card())
                        print ("Dealer drew the card: " + "[" + str(dealer.hand[-1]) + "]" +
                               " Hand value: " + str(dealer.card_sum))
                        print("--------------------", " ", sep="\n")

                        if playerBJ.card_sum == dealer.card_sum:
                            print ("The value of dealer's hand is " + str (dealer.card_sum) + " " + str (dealer.hand))
                            print (
                                "The value of your hand is " + str (playerBJ.card_sum) + " " + str (playerBJ.hand))
                            print ("Hand ended with a tie")
                            print ("--------------------", " ", sep="\n")
                            continue

                        if dealer.card_sum > 21:
                            print("Dealer has in his hand: " + str(dealer.hand) + 
                            ". Score: " + str(dealer.card_sum))
                            print("You won! " + '\U0001F37E' + '\U0001F37E' + '\U0001F37E')
                            print("--------------------", " ", sep="\n")
                            playerBJ.add_chips(betBJ)
                            chips += betBJ
                            break
                        continue
                    else:
                        print("Bravo, " + str(playerBJ.fname) +
                              "! You won " + '\U0001F37E' + '\U0001F37E' + '\U0001F37E')
                        print("--------------------", " ", sep="\n")
                        playerBJ.add_chips(betBJ)
                        chips += betBJ
                        break
                
                if dealer.card_sum == 21:
                    print("Dealer has BlackJack! You lost " + '\u2639')
                    print("--------------------", " ", sep="\n")
                    playerBJ.subtract_chips(betBJ)
                    chips -= betBJ
                    dealer.A = 0
                    break

                if dealer.card_sum > playerBJ.card_sum and dealer.card_sum <=21:
                    print("Dealer won " + '\u2639')
                    print("--------------------", " ", sep="\n")
                    playerBJ.subtract_chips(betBJ)
                    chips -= betBJ
                    break
                break

    print("You've lost all your money " + '\U0001F4B8' + '\U0001F4B8' + '\U0001F4B8' + '  \u2639')


### With the <new_game> function we ask the player if s/he wants to play again
def new_game():
    global players_list
    again = input("Would you like to play again? Type [YES] to continue " + '\U0001F600')
    print ("--------------------", " ", sep="\n")
    if again == ("yes" or "Yes" or "YES" or "Y" or "y"):
        players_list.clear()
        players_list = players_bj()
        blackjack()
        new_game()
    else:
        print("OK! Return when you have more money " + '\U0001F4B0' + '\U0001F4B0' + '\U0001F4B0')


### Este creata functia 'incepe_joc' prin care apelam functiile 'blackjack' si 'runda_noua'
# Prima oara este apelata functia 'blackjack()', care initializeaza jocul
# Dupa ce jucatorul pierde toate chipsle, este apelata functia 'runda_noua', care initializeaza o noua runda
def start_game():
    start_bj = input(
    "Would you like to play a game of Blackjack? Type [YES] to start") 
    if start_bj == ("yes" or "Yes" or "YES" or 'Y' or 'y'):
        print("Yaaay! Let's play!", "--------------------", sep="\n")
        print('  \u2660 '+ '\u2661 '+ '\u2662 '+ '\u2663 ' + '\u2660 ' + '\u2661 ' +'\u2662 '+ '\u2663 ',
    '  \u2660 '+ ' BLACKJACK  ' + '\u2663',
    '  \u2660 '+ '\u2661 '+ '\u2662 '+ '\u2663 ' + '\u2660 ' + '\u2661 ' +'\u2662 '+ '\u2663 ',
    sep='\n')
        print("--------------------", " ", sep="\n")
        blackjack()
        new_game()
    else:
        print("Alright... We will play another time " + '\u2639') 



start_game()



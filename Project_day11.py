### START

import random
from art import logo21
from replit import clear
clear()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer():
    return random.choice(cards)

def add_card(lst):
    lst.append(random.choice(cards))


## THE USER AND COMPUTER SHOULD EACH GET 2 RANDOM CARDS


#ADD UP THE USERS AND BOT SCORES


## DOES USER OR BOT HAVE A BLACKJACK?

def turn():
    # end_code = 999
    clear()
    print(logo21)
    deck_usr, deck_bot = [dealer(),dealer()] , [dealer()]
    end_game = False
    user_stop = False
    i=-1
    while not end_game:
        i+=1
        sum_usr, sum_bot = sum(deck_usr),sum(deck_bot)
        if i == 0 or user_stop == False:
            print(F"Your cards: {deck_usr}, Current score:: {sum_usr}")
        if i == 0: 
            print(F"Computer first card:: {deck_bot[0]}")            
        if sum_usr > 21:
            if 11 in deck_usr and sum_usr != 22:
                deck_usr_ace = deck_usr
                deck_usr_ace[deck_usr.index(11)] = 1
                deck_usr = deck_usr_ace
                if sum(deck_usr) <= 21:
                    end_game = True
                    # end_code = 1
                else:
                    end_game = True
                    # end_code = 2
            elif deck_usr == [11,11]:
                deck_usr = [1,11]
                sum_usr = 12
            else:
                    end_game = True
                    # end_code = 3
        elif sum_bot > 21:
            if 11 in deck_bot and deck_bot != [11,11]:
                deck_bot_ace = deck_bot
                deck_bot_ace[deck_bot_ace.index(11)] = 1
                deck_bot = deck_bot_ace
                sum_bot = sum(deck_bot)
                if sum(deck_bot) == 21:
                        end_game = True
                        # end_code = 4
                # else:
                #     end_game = True
                #     end_code = 8
            elif deck_bot == [11,11]:
                deck_bot = [1,11]
                sum_bot = 12
            else:
                    end_game = True
                    # end_code = 5

        else:
            if  user_stop==False:
                if input("Do you want another card? (Y/N) ").upper() == "Y":
                    user_stop = False
                    add_card(deck_usr)
                else:
                    user_stop = True
                    if sum_bot <17:
                        add_card(deck_bot)
            else:
                if sum_bot <17:
                    add_card(deck_bot)
                else:
                    end_game = True
                    # end_code = 6
        if end_game == True:
            #print(end_code)
            if i > 0:
                print(F"Computer final hand:: {deck_bot}, final score: {sum_bot}")
            if (sum_usr > 21) and (sum_bot > 21):
                print("It's a draw!")
            elif sum_usr == sum_bot:
                print("It's a draw!")
            elif (sum_usr > 21):
                print("You went over. You lose 😭")
            elif (sum_bot > 21):
                print("Opponent went over. You win 😁")
            else:
                if sum_usr > sum_bot:
                    print("You win 😃")
                else:
                    print("You lost!")
            if input("Do you want to play a game of Blackjack? (Y/N) ").upper() == "Y":
                turn()


turn()
            
            

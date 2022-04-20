from p14_project_data import dfInstagram
from art import logoHL, vs
import random
from replit import clear



def inequalizer(a,b):
    ''''
    Function to make sure 2 records are not the same
    '''
    while a == b:
        b = random.randint(1,49)        
    return(a, b)
    
def randomizer():
    ''''
    Function to pick two records
    '''
    randA, randB = inequalizer(random.randint(1,49), random.randint(1,49))
    recA = dfInstagram[randA]
    recB = dfInstagram[randB]
    return(recA, recB, randA, randB)



def gamerun():
    ''''
    Main game function
    '''
    count_right = 0
    end_game = False
    while end_game is False:
        clear()
        print(logoHL)
        
        recA, recB, randA, randB = randomizer()
        if count_right > 0:
            print(f"You are right! Current score: {count_right}")
            if right == "A":
                randA, randB = inequalizer(previous, randB)
                recA, recB = dfInstagram[randA], dfInstagram[randB]
            elif right == "B":
                randA, randB = inequalizer(previous, randA)
                recA, recB = dfInstagram[randA], dfInstagram[randB]
        
            

        print(f"Compare A: {recA['name']}, {recA['description']}, from {recA['country']} ")
        print(vs)
        print(f"Against B: {recB['name']}, {recB['description']}, from {recB['country']} ")
        #print(recA['follower_count'],recB['follower_count'])
        guess = input("Who has more followers? Type 'A' or 'B': ")
        
        
        if guess == 'A':
            if int(recA['follower_count']) > int(recB['follower_count']):
                count_right += 1
                previous = randA
                right = "A"
            else: 
                end_game = True
        if guess == 'B':
            if int(recB['follower_count']) > int(recA['follower_count']):
                count_right += 1
                previous = randB
                right = "B"
            else: 
                end_game = True

    if end_game:
        clear()
        print(logoHL)
        print(f"Sorry, that's wrong! Final score: {count_right}")

gamerun()
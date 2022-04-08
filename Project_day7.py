import random
import words_list as wl

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

#word_list = ["ardvark","baboon","camel"]

#STEP 1 Choose random word fro the wordlist

chosen_word = random.choice(wl.list)
#print(chosen_word)

chosen_word_list = list(chosen_word)
#print(chosen_word_list)

spaces_list = []
for i in range(0,len(chosen_word)):
    spaces_list.append("_")
#print(' '.join(spaces_list))

#STEP 2 Ask user to guess a latter and assign answer to a variable called guess. Make guess lowercase

hangman_complete = False
hangman_count = 0

while not hangman_complete == True:
    
    guess = input("\nPlease, guess a letter: ").lower()

    #STEP 3 - Check if the letter is among the chosen_word

    if guess in chosen_word_list:
        right_guess_list = []
        print("\nYou got it right!\n")
        for idx, val in enumerate(chosen_word_list):
            if guess == val:
                right_guess_list.append(idx)
        #print(right_guess_list)
        for idx, letter in enumerate(spaces_list):
            for i in right_guess_list:
                spaces_list[i] = guess
        #print(' '.join(spaces_list))


    else:
        print(f"\nSorry, no letter '{guess}' in the word!\n")
        hangman_count += 1
    
    if spaces_list.count("_") < 1:
        hangman_complete = True
        Output = "Won"

    if hangman_count == 6:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|  \O/  ")
        print("|   |   ")
        print("|  / \  ")
        print("|       ")
        print("--------\n")
        hangman_complete = True
        Output = "Lost"
    elif hangman_count == 5:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|  \ /  ")
        print("|   |   ")
        print("|  / \  ")
        print("|       ")
        print("--------\n")
    elif hangman_count == 4:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|  \    ")
        print("|   |   ")
        print("|  / \  ")
        print("|       ")
        print("--------\n")
    elif hangman_count == 3:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|       ")
        print("|   |   ")
        print("|  / \  ")
        print("|       ")
        print("--------\n")
    elif hangman_count == 2:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|       ")
        print("|       ")
        print("|  / \  ")
        print("|       ")
        print("--------\n")
    elif hangman_count == 1:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|       ")
        print("|       ")
        print("|  /    ")
        print("|       ")
        print("--------\n")
    elif hangman_count == 0:
        print(' '.join(spaces_list))
        print("\n|____   ")
        print("|   |   ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("--------\n")    

if hangman_complete == True:
    print("\nGame Over!\n")
    print(f"You {Output} !\n")
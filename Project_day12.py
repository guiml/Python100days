import random
from replit import clear

def end_game():
    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again == "y":
        game()
    else:
        exit

def game():
    clear()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")

    difficulty_levels = {
        "easy": 10,
        "hard": 5
    }

    level = difficulty_levels[difficulty]

    secret_number = random.randint(1,100)
    #print(secret_number)
    win = False
    while not level <= 0:

        print(f"You have {level} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == secret_number:
            level = 0
            win = True
        elif guess < secret_number:
            print("Too low")
        else:
            print("Too high.")
        level -= 1
    
        if level > 0:
            print("Guess again")
        elif win:
            print('You won!')
            end_game()
        else:
            print("You lost")
            end_game()

game()



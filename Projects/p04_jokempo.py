import random
## ROCK, PAPER OR SCISSORS GAME by Guilherme Louzada

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if user_choice not in (["0","1","2"]):
    print("You typed an invalid number, you lose!")
else:
    user_choice_i = int(user_choice)
    if user_choice_i == 0:
        print("""
    _______
---'   ____)
    (______)
    (______)
    (_____)
---.__(___)
        """)  
    elif user_choice_i == 1:
        print("""
    _______
---'    ____)_
        ______)
        _______)
        _______)
---.__________)
        """)
    elif user_choice_i == 2:
        print("""
    _______
---'   ____)__
        _________)
    _____________)
    (____)
---.__(___)
        """)        

    print("\nComputer chose:\n")

    computer_choice_i = random.randint(0,2)
    #print(computer_choice_i)

    if computer_choice_i == 0:
        print("""
    _______
---'   ____)
    (______)
    (______)
    (_____)
---.__(___)
            """)  
    elif computer_choice_i == 1:
        print("""
    _______
---'    ____)_
        ______)
        _______)
        _______)
---.__________)
        """)
    elif computer_choice_i == 2:
        print("""
    _______
---'   ____)__
        _________)
    _____________)
    (____)
---.__(___)
        """)    

    if ((user_choice_i == 0) & (computer_choice_i == 2)) or ((user_choice_i == 1) & (computer_choice_i == 0)) or ((user_choice_i == 2) & (computer_choice_i == 1)):
        print(f"You win!\n")
    elif ((user_choice_i == 0) & (computer_choice_i == 1)) or ((user_choice_i == 1) & (computer_choice_i == 2)) or ((user_choice_i == 2) & (computer_choice_i == 0)):
        print(f"You lose!\n")
    else:
        print(f"Draw.\n")
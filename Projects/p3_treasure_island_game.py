from re import L


print('''

 W E L C O M E  T O  T H E
 _________________________
|  .....................  |
|/----------------------\\ |
|"""""":""""":"""":"""""" |
| `.    .    :    .    .' |
|   `.   .   :   .   .'   |
|     `.  .  :  .  .'     |
|       `. . : . .'       |
|         `..:..'         |
|           `:'           |
|_________________________|
|      T R E A S U R E    |
|        I S L A N D      |
|         G A M E         |
|-------------------------|

''')

print("Welcome to the Treasure Island. \nYour Mission is to find the treasure.\n \n")

choice1 = input("\n\nYou are entering the game maze, you can turn to the left or to the right, where do you go?\n")

if choice1.lower() == "left":
    choice2 = input("\n\nCongratulations, you chose the right direction!\nNow there is a pond in front of you, would you rather swim or wait?\n")
    if choice2.lower() == "wait":
        choice3 = input("\n\nCongratulations, you chose the right direction!\nNow there are 3 doors, a Red, Yellow and a Blue one, which do you chose?\n")
        if choice3.lower() == "red":
            print("\n\nThis room is on fire, call the firefighters.\n")
            print('''
                .-""""""-.
              .'          '.
             /   O      O   \\
            :           `    :
            |G A M E  O V E R|  
            :    .------.    :
             \  '        '  /
              '.          .'
                '-......-'            
            ''')
        elif choice3.lower() == "blue":
            print("\n\nRoom is full of beasts, run so you are not eaten by them.\n")
            print('''
                .-""""""-.
              .'          '.
             /   O      O   \\
            :           `    :
            |G A M E  O V E R|  
            :    .------.    :
             \  '        '  /
              '.          .'
                '-......-'            
            ''')
        elif choice3.lower() == "yellow":
            print("\n\nCongratulations, you just won!")
        else:
            print("Game Over!\n")
            print('''
                .-""""""-.
              .'          '.
             /   O      O   \\
            :           `    :
            |G A M E  O V E R|  
            :    .------.    :
             \  '        '  /
              '.          .'
                '-......-'            
            ''')
            
    else:
        print("\n\nOh no! You were attacked by a trout and needed to head home to heal.\n")
        print('''
                .-""""""-.
              .'          '.
             /   O      O   \\
            :           `    :
            |G A M E  O V E R|  
            :    .------.    :
             \  '        '  /
              '.          .'
                '-......-'            
            ''')
else:
    print("\n\nOh no! You chose a door that let you out of the maze!\n")
    print('''
                .-""""""-.
              .'          '.
             /   O      O   \\
            :           `    :
            |G A M E  O V E R|  
            :    .------.    :
             \  '        '  /
              '.          .'
                '-......-'            
            ''')



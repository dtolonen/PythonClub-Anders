'''

Game Play:
    - The game starts with a instruction printed out, says `"This game is ....."`
    - After that is the stats of the player and enemy
    - Player plays first, start choosing action
    - At this point, only attack, after choose attack, enemy will take damage
    - Recalculate HP
    - Print out the result of this turn, how many damages has been caused by player to enemy
    - Enemy's turn
    - Call generate damage from enemy, player will take damage
    - Recalculate HP
    - Print out the result of this turn, how many damages has been caused by enemy to player
    - Print out the new stats of player and enemy
    - Check hp of player and enemy, whose hp == 0, lost
    - If hp != 0, start the loop again

'''

# Imports ------------------------------------

import \
    random  # so, this is the same import as in the game_classes.py file, but do I need it in both or does one file inherit the imports of another file in Python?
from game_classes import \
    Person  # note that you don't need the file extension game_classes.py ... is this because the files are in the same directory?

# Instantiate objects ---------------------------

# ok, so what other objects would I have to instantiate except players? See the medium/hard version examples if they have more. Yeah, there are whole subcategories - players, items, magic - before you get to the 'start game loop' section.

main_player = Person("Superman", 500, 100, 50)
enemy = Person("Bad guy", 800, 70, 30)

# Main game ---------------------------------

# 1. Intro to game with opening stats for all

print('--------------------------------')
print('\t Welcome to the game! ')
print("\t Let's defeat the bad guys! ")
main_player.get_stats()  # so, this applies the get_stats() method to the main_player object? Hmm...getting an error here "Person object has no attribute get_stats". I noticed that all my methods had not been indented - as they're supposed to be inside the class Person - except for __init__. This seems to have corrected the error. Well, no. The game allows the main_player to start, but gives the same error now for the enemy. Hold on! The error states 'take_damage,' not 'take_dmg' as in game_classes.py. Ok, this was my typo on line 85 of main.py. Ok, the easy games works! (can't select 2 as attack yet - 'list index out of range').

enemy.get_stats()  # and the same for the enemy
print('--------------------------------')

# 2. Start the game loop

running = True  # see 2.d where this is evaluated in the round summary's 'running=False' lines
while running:

    # 2.a main player starts first (Note! the rest must be INDENTED inside 2. Start the game loop!)
    print('--------------------------------')
    print(
        f'\t {main_player.name.upper()}')  # so, we're drilling down to the main_player instance of the Person class in game_classes.py and within it, we're (calling?) the name (element?) and then applying the upper (method?) to it and printing the whole lot.
    main_player.choose_action()  # so just applying the choose_action method to the main_player object
    choice_input = input("\t\t\t Choose a number: ")
    index = int(choice_input) - 1  # negatively incrementing a counter from the number the user types into choice_input
    print(f'\t You chose {main_player.action[index]}')
    # Hmm, here's that action in game_classes.py - why is it action and not choose_action?

    # 2.b Physical attack from player
    # so, this is just executing what was chosen in 2.a
    # I need to clarify the index in 2.a to properly understand the if else here.
    if index == 0:
        dmg = main_player.generate_atk_dmg()
        enemy.take_dmg(dmg)

        print(f'\t You attacked and dealt to {enemy.name} {dmg} points of damage.')

    else:
        print("This is the easy mode, you cannot choose another option for now.")
        continue

    # 2.c Enemy's turn

    print('--------------------------------')
    print(f'\t {enemy.name.upper()}')
    enemy_choice = random.randrange(0,
                                    len(
                                        enemy.action))  # applying the randrange method from the random module to the enemy_choice variable, using the range of 0 to enemy.action - there's that action (element?) from game_classes.py again.
    if enemy_choice == 0:
        enemy_dmg = enemy.generate_atk_dmg()
        main_player.take_dmg(enemy_dmg)
        print(
            f'\t {enemy.name.capitalize()} attacked and dealt to you {enemy_dmg} points of damage.'
        )

    # 2.d Summary of round

    main_player.get_stats()  # updated from the beginning
    enemy.get_stats()  # also for the enemy

    # however, first, we need to find out who won
    # what is the 'running' boolean? For the game loop to continue (to 'run') to another round of the game? If neither == 0, then the game continues until one player == 0. Ah! Look way up to 2. Start the game loop: it has a variable running = True and then a while loop 'while running'. Hmm, wasn't writing this stuff in the same order as in the example file.' Also, note the indentation: 2.a

    if main_player.hp == 0:  # (see game_classes.py) so, hp is not a method, but a var containing the main_player hp. so, you can apply vars/properties of some kind to the main_player object, too, not just methods?
        print('\t\t YOU LOST!')
        running = False
    elif enemy.hp == 0:
        print('\t\t YOU WON!')
        running = False

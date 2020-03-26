# Test
# the read me doesn't indicate this until the Medium mode, but the easy mode file has this, to generate enemy choices, I guess.
import random

''' 8 attributes: they go inside the __init__ method,	but only 4 found in the parens of the easy mode game_classes.py file. Guess the rest are made from these? What about action though - it's not in the parens. Below in the example, choose_action only prints and here self.action = ["Attack"], so also only prints?

  	- name - string 
  	# name in paren, self.name in method, wonder if order is important...self.name was last in easy mode example.

    - hp - int 
    # hp in paren, also self.hp = (hp) in method
    - max_hp - int( = hp) 
    # not in parens, self.maxhp = hp in method

    - mp - int
    # mp in parens, self.mp = mp in method 
    - max_mp - int (= mp)
    # not in parens, but self.maxmp = mp in method

    - atk_high = atk + 10
    # only atk in parens, self.atkh = atk + 10 in method
    - atk_low = atk - 10
    # only atk in parens, self.atkl = atk - 10 in method

    - action - list of string: at this level, only ["Attack"]
    # not in parens, but self.action = ["Attack"] in method
    '''


class Person:
    def __init__(self, name, hp, mp,
                 atk):  # (left the action (parameter) out in the end ) let's see what happens if I do include action, unlike the example, though probably unnecessary.Well, actually, see the game.py med/hard example class Person. It doesn't have action in there either, but under self.action, it lists ["Attack","Magic","Items"], so you can have more under self.action.

        # name, let's see about the order, unlike the example. Again, you have to assign it (... = name), as this is all about creating instances.
        self.name = name

        # hp - hp and max_hp versions, still fuzzy ab these
        self.hp = hp
        self.maxhp = hp

        # mp - mp and max_mp versions. This just mirrors hp?
        self.mp = mp
        self.maxmp = mp

        # atk - high and low versions
        self.atkh = atk + 10  # So, it's ok to change name to atkh?
        self.atkl = atk - 10
        # action
        self.action = ["Attack"]

    # still inside the class Person, it has 4 methods:
    # Again, these are in different order to the example, let's see if it matters.

    def get_stats(
            self):  # to print out current stats: name, HP/MaxHP, MP/MaxMP. NOTE! need to pass self in parens! All of these take self, but oddly take_damage(self, dmg) and generate_atk_damage(self) - actually, makes some sense, once you've created the generate_dmg method, which includes a variable dmg. The take_damage method then uses that variable dmg.
        print(
            self.name)  # let's see if this would be enough. On next line, I'll add the example's f string version, commented out and with single quotes, not double ones as in the example.
        print(f'\t\t {self.name.upper()}')
        # and then just repeat this for the next two items.
        print(f'\t\t\t {self.hp}/{self.maxhp}')
        print(f'\t\t\t {self.mp}/{self.maxmp}')

    def choose_action(
            self):  # print out all the action options in the action list to the terminal, at this stage is to print out from ["Attack"]

        # wondering what the first line 'number = 1' in the method is. Maybe try to create 2 numbers/items, 2 being magic, to see if that's what 1 means. If not, delete no 2.

        number = 1
        print('\t\t ACTION: ')
        for element in self.action:
            print(f'\t\t\t{number}: {element}')
            number = number + 1

    def generate_atk_dmg(
            self):  # return a attack damage value, randomly between atk_high and atk_low. Note that we're now utilising that 'import random' module line at the beginning and that, I guess, randrange takes values from between self.atkl and self.atkh.
        dmg = random.randrange(self.atkl, self.atkh)
        return dmg

    def take_dmg(self,
                 dmg):  # note different method name to the example's take_damage. Maybe more in line with the above, which uses dmg, too. Take into a damage value and calculate the HP loss and return new HP points
        self.hp = self.hp - dmg
        if self.hp < 0:  # note why no elif or else named?
            self.hp = 0
        return self.hp





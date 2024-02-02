#random output of 2 dice pgm

import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
both_dice = Dice()
print(both_dice.roll())


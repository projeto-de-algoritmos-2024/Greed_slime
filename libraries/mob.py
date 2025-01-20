import random


"""

This is the codes for the characters :P

to create a new character(enemy or friend) you have to start with:

name: string, just a name for the character
species:
    for now there are 5 species:
        - slime( friendly only)
        - big_slime
        - skull
        - templar
        - lich

job:
    the character class( only for allies ):
        - thief( faster)
        - hero( balanced)
        - tank( stronger, but slower)
        - archer( weaker, but with good sp_atk)
        - mage( weaker and just like a archer, but cooler)

"""



atk = 0
sp_atk = 1
defense = 2
sp_def = 3
spd = 4
acc = 5



class Mob():
    def __init__(self, name, species, job, level):
        self.name = name
        self.species = species
        self.job = job
        self.level = level
        self.stats = [ int(10*random.random()), int(10*random.random()),int(10*random.random()), int(10*random.random()),int(10*random.random()), int(10*random.random()) ]

    def update(self):
        pass


class Player():
    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour
        #self.icon = slime_down

    def update(self):
        pass


class Enemy():
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type


    def move():
        pass

    def draw():
        pass

    
    def update(self):
        self.move()
        self.draw()
        pass
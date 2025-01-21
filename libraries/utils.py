#written by bcl0c, whose utils will actually destroy your system32 when you're looking away.
import random
from mob import Mob as mob

zetta = mob(1, 2, 3, 4)
print(zetta.stats['atk'])

def attackConnected(chance):
    if chance > 100: return False
    rng = random.randint(0, 100)
    connected = True if rng > chance else False
    return connected

def attack(mob1: mob, mob2: mob):
    """
        attack function ->
            returns attack based on various stats and factors. 
    """
    chance = 1/mob2.stats['inv_spd']
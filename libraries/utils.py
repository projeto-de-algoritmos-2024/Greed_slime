#written by bcl0c, whose utils will actually destroy your system32 when you're looking away.
import random
from mob import Mob

def attackConnected(chance):
    if chance > 100: return False
    rng = random.randint(0, 100)
    connected = True if rng > chance else False
    return connected

def attack(mob1: Mob , mob2: Mob):
    """
        attack function ->
            returns attack based on various stats and factors. 
    """
    chance = mob2.
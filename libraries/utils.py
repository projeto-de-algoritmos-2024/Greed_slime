#written by bcl0c, whose utils will actually destroy your system32 when you're looking away.
import random
from mob import Mob as mob
import pygame as pg

DEBUG = True
FPS = 60
WIDTH = 640
HEIGHT = 640
vec = pg.math.Vector2
mask = pg.Color(254,255,255)
empty = pg.Color(0,0,0,0)
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
    chance = (1/mob2.stats['inv_spd'] * 100 ) % 100 #smaller inv_spd means better, so the chance of 
    chance = int(chance)
    if DEBUG:
        print(chance)
    damage = 0
    if attackConnected(chance):
        if mob1.job != 'mage':
            damage = mob2.stats['defense'] - mob1.stats['atk']
            return damage
        else:
            damage = mob2.stats['sp_def'] - mob1.stats['sp_atk']
            return damage
    return damage
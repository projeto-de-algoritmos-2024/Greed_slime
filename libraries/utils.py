#written by bcl0c, whose utils will actually destroy your system32 when you're looking away.
import random
from mob import Mob as mob
import pygame as pg

RUN_CONST = "RUN"
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

def analyse(yourparty: list, enemies: list):
    """
        analyses the damage type from enemies and returns what should you focus on.
        input:
            yourparty -> 3x2 list of allied mobs
            enemies -> 3x2 list of enemies

            the list[0] represents the first layer of the party 
            the list[1] represents the second layer

            All list[1] enemies are cqc untouchable until you kill the first layer.
        output:
            order -> 
    """
    allied_sp_def = 0
    allied_def = 0
    allied_atk = 0
    allied_sp_atk = 0
    allied_rangeds = 0

    enemy_sp_def = 0
    enemy_def = 0
    enemy_atk = 0
    enemy_sp_atk = 0
    for ally in yourparty:
        allied_sp_def += ally.stats['sp_def']
        allied_def    += ally.stats['defense']
        allied_atk    += ally.stats['atk']
        allied_sp_atk += ally.stats['sp_atk']
        if ally.job == 'mage' or ally.job == 'archer':
            allied_rangeds += 1
    for enemy in enemies:
        enemy_sp_def += enemy.stats['sp_def']
        enemy_def    += enemy.stats['def']
        enemy_atk    += enemy.stats['atk']
        enemy_sp_atk += enemy.stats['sp_atk']
    
    if len(enemies[1]) != 0: #means we got to take into consideration the party rangers (mage and archer)
        if allied_rangeds > 3 and enemy_def < allied_atk:
            enemies.sort(key = lambda x: x.stats['def'])
            layer = enemies[0]
            enemies[0] = enemies[1]
            enemies[1] = layer
            return enemies
        elif allied_rangeds > 3 and enemy_sp_def < allied_sp_atk:
            enemies.sort(key = lambda x: x.stats['sp_def'])
            layer = enemies[0]
            enemies[0] = enemies[1]
            enemies[1] = layer 
            return enemies
        else:
            return "RUN" #means you got absolutely no leverage against these enemies.
    else:
        if allied_atk > enemy_def:
            return enemies.sort(key = lambda x: x.stats['def'])
        elif allied_sp_atk > enemy_sp_atk:
            return enemies.sort(key = lambda x: x.stats['sp_def'])
        else: 
            return "RUN" #same here, you got no leverage.
    

# by Ryan Augusto Brandão Salles & Víctor Moreira Almeida

#import pygame as pg
import math as mt
import sys
#from pygame.locals import *
import random
from libraries.default_values import *
import libraries.game as game
import libraries.titleScreen as ts






"""

#pygame sera implementado dps


pg.init()
FramePerSec = pg.time.Clock()


displaysurface = pg.display.set_mode((WIDTH, HEIGHT))
icon = pg.image.load('assets/icon.png')
pg.display.set_icon(icon)
pg.display.set_caption("Slime dungeon run!")

gameover = False

def draw():
    pass

while(True):
    titlescreen = ts.TitleScreen()
    jogo = []

    while(not titlescreen.play):
        titlescreen.update()
        displaysurface.blit(titlescreen.surf,(0,0))
        pg.display.update()

    for jooj in jogo:

        while(True):
            #update_joystick()
            #print(controller.get_button(0))
            displaysurface.fill((0,0,0))
            jooj.update()
            displaysurface.blit(jooj.surf,(0,0))
            pg.display.update()
            FramePerSec.tick(FPS)
            if jooj.exit:
                gameover = jooj.gameover
                if gameover:

                    break
                #jooj.song.stop()
                break
        if gameover: break

"""


if __name__ == "__main__":
    print("Hello world!")
    pass
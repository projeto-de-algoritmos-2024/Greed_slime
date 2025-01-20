import pygame as pg

# temporary code :3


FPS = 60
WIDTH = 640
HEIGHT = 640
vec = pg.math.Vector2
mask = pg.Color(254,255,255)
empty = pg.Color(0,0,0,0)


# end of temporary codes





# slimes

slime_hero = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]
slime_thief = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]
slime_tank = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]
slime_archer = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]
slime_mage = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]
slime_hero = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
    ]


# enemies

big_slime = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
]
lich = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
]
skull = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
]
templar = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,64))
]

background = [
    pg.transform.scale(pg.image.load('assets/hero_down.png'), (WIDTH,HEIGHT))
]

"""


class Projectiles(pg.sprite.Sprite):
    def __init__(self, typeR, side):
        super().__init__() 
        self.type = typeR
        self.speed = 4
        self.side = side
        self.icon = arrow_up
        self.surf = pg.Surface((64,64))
        self.surf.set_colorkey(mask)
        self.surf.fill(empty)
        self.rect = self.icon.get_rect()
        self.pos = vec((0,0))
        self.face(side)


"""



def giveSprites(species, job):
    surf = pg.surface((64,64))

    if species == "big_slime":
        images = big_slime
    if species == "skull":
        images = skull
    if species == "lich":
        images = lich
    if species == "templar":
        images = templar
    if species == "slime":
        if job == "archer":
            images = slime_archer
        if job == "hero":
            images = slime_hero
        if job == "archer":
            images = slime_mage
        if job == "archer":
            images = slime_tank
        if job == "archer":
            images = slime_thief

    icon = images[0]
    surf.set_colorkey(mask)
    surf.fill(empty)
    rect = icon.get_rect()




    return [ surf, rect ]
    pass
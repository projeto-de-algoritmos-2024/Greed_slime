import mob
import map
from default_values import *



class game():
    def __init__(self):
        self.map = map.map[0]
        self.player = mob.player(self.map.find('s'), "blue")
        pass

    def update(self):
        pass
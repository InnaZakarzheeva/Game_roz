
from pygame import *
import os
import pyganim

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__) #  Повний шлях до каталогу з файлами

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/p.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class BlockDie(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.image=image.load("%s/blocks/i.png" % ICON_DIR)

class Test(Platform):
    def __init__(self, x, y):
        Platform.__init__(self,x,y)
        self.image=image.load("%s/blocks/t.png" % ICON_DIR)
        
    

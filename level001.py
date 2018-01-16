#! /usr/bin/env python

__author__ = 'esteban'
"""
Reference
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
"""
import levels

class Level(levels.Level):
    """Level 1 of the PyMan Game"""

    def __init__(self):
        self.BLOCKH = 9
        self.BLOCKV = 8
        self.BLOCKSI = 1
        self.BLOCKSD = 2
        self.BLOCKII = 3
        self.BLOCKID = 4
        self.SNAKE = 10
        self.PELLET = 0
        self.MONSTER = 6
        self.SCARED_MONSTER = 7
        self.SUPER_PELLET = 5
        self.FRUTA = 11

    def get_layout(self):
        return [[1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2],\
                [8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8],\
                [8, 0, 1, 2, 0, 1, 9, 9, 2, 0, 8,6,99, 6,99, 6, 8, 0, 1, 9, 9, 2, 0, 1, 2, 0, 8],\
                [8, 0, 3, 4, 0, 3, 9, 9, 4, 0, 3,99,6,99,99,99, 4, 0, 3, 9, 9, 4, 0, 3, 4, 0, 8],\
                [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],\
                [8, 0, 9, 9, 0, 1, 2, 0, 1, 9, 2, 0, 1, 9, 2, 0, 1, 9, 2, 0, 1, 2, 0, 9, 9, 0, 8],\
                [8, 0, 1, 2, 0, 3, 4, 0, 3, 9, 4, 0, 3, 9, 4, 0, 3, 9, 4, 0, 3, 4, 0, 1, 2, 0, 8],\
                [8, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 8],\
                [8, 0, 8, 8, 0, 1, 2, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2, 0, 1, 2, 0, 8, 8, 0, 8],\
                [8, 0, 8, 8, 0, 8, 8, 0, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4, 0, 8, 8, 0, 8, 8, 0, 8],\
                [8, 0, 3, 4, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 3, 4, 0, 8],\
                [8, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 0, 1, 9, 2, 0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 8],\
                [8, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 8],\
                [8, 0, 8, 8, 0, 1, 9, 9, 2, 0, 0, 0, 0,10, 0, 0, 0, 0, 0, 1, 9, 2, 0, 8, 8, 0, 8],\
                [8, 0, 8, 8, 0, 3, 9, 9, 4, 0, 1, 9, 9, 9, 9, 9, 2, 0, 0, 3, 9, 4, 0, 8, 8, 0, 8],\
                [8, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 4, 0, 0, 0, 0, 0, 0, 3, 4, 0, 8],\
                [8, 5, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 0,11, 0, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 5, 8],\
                [3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 4]]            
   
    def get_sprites(self):
        blockh, rect = self.load_image('bloqueh.png')
        blockv, rect = self.load_image('bloquev.png')
        blocksi, rect = self.load_image('bloquesi.png')
        blocksd, rect = self.load_image('bloquesd.png')
        blockii, rect = self.load_image('bloqueii.png')
        blockid, rect = self.load_image('bloqueid.png')
        pellet, rect = self.load_image('pellet.png', -1)
        snake, rect = self.load_image('snake.png', -1)
        monster_01, rect = self.load_image('phantom.png', -1)
        monster_scared_01, rect = self.load_image('phantomAzul.png', -1)
        super_pellet, rect = self.load_image('super_pellet.png', -1)
        fruta, rect = self.load_image('fruta.png', -1)
        return [pellet, blocksi, blocksd, blockii, blockid, super_pellet, monster_01, monster_scared_01, blockv, blockh, snake, fruta]
        
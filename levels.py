#! /usr/bin/env python
# This Python file uses the following encoding: utf-
__author__ = 'esteban '
"Fuente:http://www.pygame.org/docs/tut/chimp/ChimpLineByLine.html"

import os
import pygame
from pygame.locals import *
class Level:
    """The Base Class for Levels"""
    def get_layout(self):
        """Get the Layout of the level"""
        """Returns a [][] list"""
        pass

    def get_images(self):
        """Get a list of all the images used by the level"""
        """Returns a list of all the images used.  The indices
        in the layout refer to sprites in the list returned by
        this function"""
        pass

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('Resources', 'Images')
        fullname = os.path.join(fullname, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()





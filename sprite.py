# This Python file uses the following encoding: utf-8
import pygame

__author__ = 'esteban'
"""
Reference
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
http://www.stealthcopter.com/blog/2010/02/advancing-pyman-using-pythons-pygame-to-recreate-pacman/
"""
class Sprite(pygame.sprite.Sprite):
    def __init__(self, center_point, image):
        """
        Constructor de la clase Sprite derivada de pygame.sprite.Sprite
        :param center_point: Posición central del rectangulo
        :param image: Imagen a mostar en el tablero
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = center_point


class Pellet(pygame.sprite.Sprite):
    def __init__(self, top_left, image=None):
        """
        Constructor de la clase Sprite derivada de pygame.sprite.Sprite
        :type self: object
        """
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image, self.rect = load_image('pellet.png', -1)
        else:
            self.image = image
            self.rect = image.get_rect()
        self.rect.topleft = top_left

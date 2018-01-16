 # This Python file uses the following encoding: utf-8
import pygame
from pygame.constants import *
import sprite

__author__ = 'Esteban Munoz,Marco Mendoza'

"""
Reference
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
http://www.stealthcopter.com/blog/2010/02/advancing-pyman-using-pythons-pygame-to-recreate-pacman/
"""

SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START + 1
SNAKE_EATEN = SUPER_STATE_OVER + 1

class Pacman(sprite.Sprite):

    def __init__(self, centerPoint, image):
        """
        Constructor de la clase Pacman
        :param centerPoint: Posición central del rectangulo
        :param image: Imagen a mostar en el tablero
        :return:
        """
        sprite.Sprite.__init__(self, centerPoint, image)
        self.pellets = 0
        self.x_dist = 16
        self.y_dist = 16
        self.xMove = 0
        self.yMove = 0
        self.superState = False
        self.original_rect = pygame.Rect(self.rect)

    def moveKeyDown(self, key):
        """
        Actualicación de movimiento
        :param key: Tipo de evento
        :return:
        """
        if key == K_RIGHT:
            self.xMove += self.x_dist
        elif key == K_LEFT:
            self.xMove += -self.x_dist
        elif key == K_UP:
            self.yMove += -self.y_dist
        elif key == K_DOWN:
            self.yMove += self.y_dist

    def moveKeyUp(self, key):
        """
        Actualicación de movimiento
        :param key: Tipo de evento
        :return:
        """
        if K_RIGHT == key:
            self.xMove += -self.x_dist
        elif K_LEFT == key:
            self.xMove += self.x_dist
        elif K_UP == key:
            self.yMove += self.y_dist
        elif K_DOWN == key:
            self.yMove += -self.y_dist

    def update(self, block_group, pellet_group, super_pellet_group, monster_group, fruta_group):
        """
        Actualización del punto cuando se hace un movimiento
        :param block_group: Puntos en el tablero
        :return:
        """
        sonidoComida = pygame.mixer.Sound("Resources/Sound/Chomp.wav")
        
        if (self.xMove == 0)and(self.yMove == 0):
            return
        self.rect.move_ip(self.xMove, self.yMove)
        
        if pygame.sprite.spritecollideany(self, block_group):
            self.rect.move_ip(-self.xMove, -self.yMove)
        
        """Check to see if we hit a Monster!"""
        lst_monsters =pygame.sprite.spritecollide(self, monster_group, False)
        lst_fruta =pygame.sprite.spritecollide(self, fruta_group, False)

        if (len(lst_fruta)>0):
            """Allright we have hit a Monster!"""
            
            sonidoComida.play()

        if (len(lst_monsters)>0):
            """Allright we have hit a Monster!"""
            self.MonsterCollide(lst_monsters)
        else:
            """Alright we did move, so check collisions"""
            """Check for a snake collision/pellet collision"""
            lstCols = pygame.sprite.spritecollide(self, pellet_group, True)
            if (len(lstCols)>0):
                """Update the amount of pellets eaten"""
                self.pellets += len(lstCols)
                sonidoComida.play()
                """if we didn't hit a pellet, maybe we hit a SUper Pellet?"""
            elif (len(pygame.sprite.spritecollide(self, super_pellet_group, True))>0):
                """We have collided with a super pellet! Time to become Super!"""
                self.superState = True
                pygame.event.post(pygame.event.Event(SUPER_STATE_START,{}))
                """Start a timer to figure out when the super state ends"""
                pygame.time.set_timer(SUPER_STATE_OVER,0)
                pygame.time.set_timer(SUPER_STATE_OVER,5000)

                
                
    def MonsterCollide(self, lstMonsters):
        """This Function is called when the snake collides with the a Monster
        lstMonstes is a list of Monster sprites that it has hit."""
        sonidoMuertePacman = pygame.mixer.Sound("Resources/Sound/Dead.wav")
        if (len(lstMonsters)<=0):
            """If the list is empty, just get out of here"""
            return
    
        """Loop through the monsters and see what should happen"""
        for monster in lstMonsters:
            if (monster.scared):
                monster.Eaten()
            else:
                """Looks like we're dead"""
                pygame.event.post(pygame.event.Event(SNAKE_EATEN,{}))
                self.rect = self.original_rect
                print(self.rect)
                sonidoMuertePacman.play()
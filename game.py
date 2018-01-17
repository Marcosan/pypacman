# -*- coding: utf-8 -*-
import os

import sys
import os.path
import level001
import random
import pygame
from pygame.locals import *
from menu import *
from pacman import *
from sprite import *
from basicMonster import Monster

BLOCK_SIZE = 32
salir = False
opciones = []
opcion_enter = 0
vidas = 2
playInicio = 0
gameover = 0

pygame.font.init()
screen = pygame.display.set_mode((850, 650))
fondo = pygame.image.load("Resources/Images/pacmanfondo.png").convert()
fondoabout = pygame.image.load("Resources/Images/about.png").convert()
fondocreditos = pygame.image.load("Resources/Images/creditos.png").convert()

"""
Reference
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
http://www.stealthcopter.com/blog/2010/02/advancing-pyman-using-pythons-pygame-to-recreate-pacman/
"""
def comenzar_nuevo_juego():
    set_opcion_enter(1)

def mostrar_opciones():
    set_opcion_enter(2)

def creditos():
    set_opcion_enter(3)

def salir_del_programa():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)

def set_opcion_enter(a):
    global opcion_enter    # Needed to modify global copy of globvar
    opcion_enter = a

class Game:



    def __init__(self, width, height):
        """Pantalla para el juego"""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        global opciones
        global gameover
        opciones = [
            ("Jugar", comenzar_nuevo_juego),
            ("Controles", mostrar_opciones),
            ("Creditos", creditos),
            ("Salir", salir_del_programa)
            ]

    def LoadSprites(self):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)
        """Load the level"""
        level1 = level001.Level()
        layout = level1.get_layout()
        img_list = level1.get_sprites()

        """Create the Pellet group"""
        self.pellet_sprites = pygame.sprite.RenderUpdates()
        self.super_pellet_sprites = pygame.sprite.RenderUpdates()
        """Create the block group"""
        self.block_sprites = pygame.sprite.RenderUpdates()
        self.monster_sprites = pygame.sprite.RenderUpdates()
        self.fruta_sprites = pygame.sprite.RenderUpdates()

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                if layout[y][x]==level1.BLOCKH:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKH])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.BLOCKV:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKV])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.BLOCKSI:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKSI])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.BLOCKSD:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKSD])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.BLOCKII:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKII])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.BLOCKID:
                    block = sprite.Sprite(centerPoint, img_list[level1.BLOCKID])
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.SNAKE:
                    self.snake = Pacman(centerPoint,img_list[level1.SNAKE])
                elif layout[y][x]==level1.PELLET:
                    pellet = sprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet) 
                elif layout[y][x]==level1.FRUTA:
                    fruta = sprite.Sprite(centerPoint, img_list[level1.FRUTA])
                    self.fruta_sprites.add(fruta) 
                elif layout[y][x]==level1.MONSTER:
                    monster = Monster(centerPoint, img_list[level1.MONSTER]
                                       , img_list[level1.SCARED_MONSTER])
                    self.monster_sprites.add(monster) 
                    """We also need pellets where the monsters are"""
                    pellet = sprite.Sprite(centerPoint, img_list[level1.PELLET])
                    self.pellet_sprites.add(pellet) 
                elif layout[y][x]==level1.SUPER_PELLET:
                    super_pellet = sprite.Sprite(centerPoint, img_list[level1.SUPER_PELLET])
                    self.super_pellet_sprites.add(super_pellet) 
        """Create the Snake group"""
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))


    def menu(self):
        import pygame
        """This is the Main Loop of the Game"""
        reg_menu = True
        opcion = 0
        sonidoInicio = pygame.mixer.Sound("Resources/Sound/Start.wav")
        """Load All of our Sprites"""
        self.LoadSprites()
        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        """Draw the blocks onto the background, since they only need to be
        drawn once"""
        self.block_sprites.draw(self.background)
        menuP = Menu(opciones)
        sonidoComidaEspecial = pygame.mixer.Sound("Resources/Sound/Scared.wav")
        global playInicio
        global gameover
        gameover = 0
        while reg_menu:
            salida = False
            reg_menu = True
            if opcion_enter == 0:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        salir = True

                screen.blit(fondo, (0, 0))
                menuP.actualizar()
                menuP.imprimir(screen)
                pygame.display.flip()
                pygame.time.delay(10)

            if opcion_enter == 1:
                if(playInicio == 0):
                    sonidoInicio.play()
                    
                
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            print("Ha salido del Juego")
                            salida = True
                            reg_menu = False
                        if event.key == K_r:
                            set_opcion_enter(0)
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if ((event.key == K_RIGHT)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                            self.snake.moveKeyDown(event.key)
                    elif event.type == KEYUP:
                        if ((event.key == K_RIGHT)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                            self.snake.moveKeyUp(event.key)
                    elif event.type == SUPER_STATE_OVER:
                        self.snake.superState = False
                        """Stop the timer"""
                        pygame.time.set_timer(SUPER_STATE_OVER, 0)
                        for monster in self.monster_sprites.sprites():
                            monster.SetScared(False)
                    elif event.type == SUPER_STATE_START:
                        for monster in self.monster_sprites.sprites():
                            monster.SetScared(True)
                            
                            sonidoComidaEspecial.play()
                    elif event.type == SNAKE_EATEN:
                        """The snake is dead!"""
                        """For now kist quit"""
                        global vidas
                        if vidas != 0:
                            vidas = vidas - 1
                        else:
                            gameover = 1
                            
                            

                """Update the snake sprite"""
                self.snake_sprites.update(self.block_sprites, self.pellet_sprites,
                                          self.super_pellet_sprites, self.monster_sprites, self.fruta_sprites)
                self.monster_sprites.update(self.block_sprites)


                """Check for a snake collision/pellet collision"""
                lstCols = pygame.sprite.spritecollide(self.snake, self.pellet_sprites, True)
                """Update the amount of pellets eaten"""
                self.snake.pellets = self.snake.pellets + len(lstCols)

                """Do the Drawging"""
                self.screen.blit(self.background, (0, 0))
                if pygame.font:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Puntaje %s" % (3*self.snake.pellets), 1, (255, 255, 255))
                    textpos = text.get_rect()
                    self.screen.blit(text, textpos.inflate(-600,-1155))
                    text_vida = font.render("Vidas %s" % vidas, 1, (255, 255, 255))
                    textpos_vida = text_vida.get_rect()
                    self.screen.blit(text_vida, textpos_vida.inflate(-20,-1155))
                    if(vidas == 0):
                        font_gameover = pygame.font.Font(None, 70)
                        text_gameover = font_gameover.render("GAME OVER", 1, (255, 255, 255))
                        textpos_gameover = text_gameover.get_rect()
                        self.screen.blit(text_gameover, textpos_gameover.inflate(-500,-500))

                self.pellet_sprites.draw(self.screen)
                self.snake_sprites.draw(self.screen)
                self.super_pellet_sprites.draw(self.screen)
                self.monster_sprites.draw(self.screen)
                self.fruta_sprites.draw(self.screen)

                pygame.display.flip()
                pygame.time.delay(50)
                if(playInicio == 0):
                    pygame.time.delay(4000)
                    playInicio = 1

            if (opcion_enter == 2):
                screen.blit(fondoabout, (0, 0))
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if (event.key == K_ESCAPE):
                            print("Ha salido del Juego")
                            salida = True
                            reg_menu = False
                        if (event.key == K_r):
                            set_opcion_enter(0)

                    if event.type == pygame.QUIT:
                        sys.exit()
                pygame.display.flip()

            if (opcion_enter == 3):
                screen.blit(fondocreditos, (0, 0))
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if (event.key == K_ESCAPE):
                            print("Ha salido del Juego")
                            salida = True
                            reg_menu = False
                        if (event.key == K_r):
                            set_opcion_enter(0)

                    if event.type == pygame.QUIT:
                        sys.exit()
                pygame.display.flip()



if __name__ == "__main__":
    Window = Game(870, 650)
    Window.menu()

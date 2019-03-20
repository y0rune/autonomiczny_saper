from typing import List, Any

import pygame
from pygame.locals import *
from random import *


class Board:
    def __init__(self, x, y):
        self.x=x    
        self.y=y
        self.board = [[None for j in range(12)]for i in range(8)]

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.x,self.y))
        pygame.display.set_caption("Saper")
        self.background=pygame.image.load('sprites/pole.png')
        self.window.blit(self.background,(0,0))
        pygame.display.update()
        self.run = True

        while (self.run):
            pygame.time.delay(100)
            self.renderSprites()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

    def addObject(self,game_object,x,y):
        self.board[y][x] = game_object

    def renderSprites(self):
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x!=None):
                    self.window(x.sprite.convert_alpha(),(index_x*100,index_y*100))

    def close(self):
        self.run = False
        pygame.quit()
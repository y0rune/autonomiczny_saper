from typing import List, Any

import pygame
from pygame.locals import *
from random import *
from modules.Board.Direction import Direction
from modules.MapObjects.Tool import Tool
from modules.Board.Point import Point
from modules.Board.DirectionCalculator import DirectionCalculator
from modules.Board.EquipmentGui import EquipmentGui

DISPLACEMENT_Y = 45
DISPLACEMENT_X = 33
SQUARE_SIZE = 100


class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[None for j in range(12)]for i in range(8)]
        self.eq_gui = EquipmentGui(1280, 125)

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Saper")
        self.background = pygame.image.load('sprites/pole.png')
        self.run = True

        while (self.run):
            pygame.time.delay(100)

            self.renderSprites()
            self.renderGui()
            pygame.display.update()

            if(not self.player.steps.empty()):
                direction = self.player.steps.get()
                self.walk(direction)

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.close()

            # Tymczasowe manulane chodzenie
                if event.type == KEYDOWN:

                    if (event.key == K_LEFT):
                        self.walk(Direction.LEFT)
                    if (event.key == K_RIGHT):
                        self.walk(Direction.RIGHT)
                    if (event.key == K_DOWN):
                        self.walk(Direction.DOWN)
                    if (event.key == K_UP):
                        self.walk(Direction.UP)

    def walk(self, direction):
        cords = self.getCordsOf(self.player)
        new_cords = DirectionCalculator.getCordsByDirection(
            cords.x, cords.y, direction)

        self.board[cords.y][cords.x].setSpriteDirection(direction)

        if(new_cords.x >= 0 and new_cords.x <= 11 and new_cords.y >= 0 and new_cords.y <= 7 and
           (self.board[new_cords.y][new_cords.x] == None or type(self.board[new_cords.y][new_cords.x]) is Tool)):
            if(type(self.board[new_cords.y][new_cords.x]) is Tool):
                self.player.pickUp(self.board[new_cords.y][new_cords.x])
            self.board[new_cords.y][new_cords.x] = self.board[cords.y][cords.x]
            self.board[cords.y][cords.x] = None
        else:
            return False

    def getCordsOf(self, object):
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x == self.player):
                    return Point(index_x, index_y)

    def addObject(self, game_object, x, y):
        self.board[y][x] = game_object

    def addPlayer(self, player_object, x, y):
        self.board[y][x] = player_object
        self.player = player_object
        self.eq_gui.setEquipment(self.player.equipment)

    def renderSprites(self):
        self.window.blit(self.background, (0, 0))
        for index_y, y in enumerate(self.board):
            for index_x, x in enumerate(y):
                if(x != None):
                    sprite = pygame.image.load(x.sprite).convert_alpha()
                    self.window.blit(sprite, (DISPLACEMENT_X + index_x*SQUARE_SIZE,
                                              DISPLACEMENT_Y + index_y*SQUARE_SIZE))

    def renderGui(self):
        renderList = self.eq_gui.getRenderList()
        for control in renderList:
            sprite = pygame.image.load(control.sprite).convert_alpha()
            self.window.blit(
                sprite, (self.eq_gui.x + control.x, self.eq_gui.y + control.y))

    def close(self):
        self.run = False
        pygame.quit()
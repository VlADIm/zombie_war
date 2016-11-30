import pygame
import time

pygame.init()

clock = pygame.time.Clock()

class House(pygame.sprite.Sprite):
    image = None
    def __init__(self, x_coor, y_coor, player_pop, player_control, connections):
        super().__init__()
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.player_pop = player_pop
        self.player_control = player_control
        self.connections = connections

        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()


    def placeHouse(self):

        self.image = pygame.Surface([100, 50])
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coor
        self.rect.y = self.y_coor
        self.image.fill((0,0,0))

    def update_pop(self):
        if(self.player_control != 'Neutral'):
            self.player_pop += 1

    def __str__(self):
        return '{} {} {}'.format(self.x, self.y, self.h)

import pygame
pygame.init()

gdisplay = pygame.display.set_mode((1200,600))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)

class house_sprite(pygame.sprite.Sprite):
    image = None
    def __init__(self, x, y):
        super().__init__()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([100, 100])
        self.image.fill(black)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y



    def update(self, control):
        if house_sprite.image is None:
           house_sprite.image = pygame.image.load('hou.png')

        if (control == 'Neutral'):
            self.image = pygame.image.load('hou.png')

        elif (control == 'Player 1'):
            self.image = pygame.image.load('redhou.png')

        elif (control == 'select'):
            self.image = pygame.image.load('redhouselect.png')


    def __str__(self):
        return '{} {} {}'.format(self.x, self.y, self.h)

import pygame

pygame.init()

class House(pygame.sprite.Sprite):
    """docstring"""
    def __init__(self, x_coor, y_coor, clicked, player_def, player_atk):
        """docstring"""
        super().__init__()
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.clicked = clicked
        self.player_def = player_def
        self.player_atk = player_atk

        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()


    def placeHouse(self):
        """docstring"""
        self.image = pygame.Surface([50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coor
        self.rect.y = self.y_coor
        self.image.fill((0,0,0))

    def checkClicked(self):
        """docstring"""
        if(self.x_coor + 100 > self.mouse[0] > self.x_coor and self.y_coor + 50 > self.mouse[1] > self.y_coor):
            if(self.click == (1,0,0)):
                self.clicked = True
            else:
                self.clicked = False
        print(self.clicked)


    def makeBorder(self):
        if(self.player_def <= 0):
            self.image = pygame.image.load('hou.png')
        elif(self.player_def > 0 and self.clicked == False):
            self.image = pygame.image.load('redhou.png')
        elif(self.player_def > 0 and self.clicked == True):
            self.image = pygame.image.load('redhouselect.png')

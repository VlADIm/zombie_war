import pygame

pygame.init()

class Button:
    def __init__(self, text, x_coor, y_coor):
        self.text = text
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def inside(self):
        if(self.x_coor+100 > self.mouse[0] > self.x_coor and self.y_coor+50 > self.mouse[1] > self.y_coor):
            return True
        else:
            return False


    def clicked(self):
        if(self.click == (1,0,0)):
            return True
        else:
            return False

    def next(self):
        if(self.inside() == True and self.clicked() == True):
            return True
        else:
            return False

import pygame
import time
import random
import sys

pygame.init()
gdisplay = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)
pygame.display.set_caption("Zombie War")

class house(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([50, 40])
        self.image.fill(black)
 
        self.rect = self.image.get_rect()
        self.rect.x = 425
        self.rect.y = 300
    def update(self, val, val2):
        if house.image is None:
           house.image = pygame.image.load('hou.png')
           
        if val <= 0:
            self.image = house.image
        else:
            self.image = pygame.image.load('redhou.png')
        
class house1(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([130, 50])
        self.image.fill(black)
 
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300
    def update(self, val, val2):
        if house1.image is None:
           house1.image = pygame.image.load('hou.png')
           
        if val2 <= 0:
            self.image = house1.image
        else:
            self.image = pygame.image.load('redhou.png')
        
class house2(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([130, 60])
        self.image.fill(red)
 
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 550
        if house2.image is None:
            house2.image = pygame.image.load('hou.png')
        self.image = house2.image
class house3(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([130, 60])
        self.image.fill(red)
 
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 100
        if house3.image is None:
            house3.image = pygame.image.load('bluehou.png')
        self.image = house3.image
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class button(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (150,550, 110, 60))
           
        else:
            pygame.draw.rect(gdisplay, lightred, (155,550, 100, 50))

        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (395,550, 130, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (400,550, 120, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Start", 1,(0,0,0))
        gdisplay.blit(btext, (160, 560))

        font3 = pygame.font.Font("freesansbold.ttf",20)
        btext= font3.render("Load Game", 1,(0,0,0))
        gdisplay.blit(btext, (405, 560))
        
class zombieupright(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 550

    def update(self, val, val2):
        self.rect.x += 1
        self.rect.y -= 3

class zombieupleft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 550

    def update(self, val, val2):
        self.rect.x -= 1
        self.rect.y -= 3
        
clicked = []       
def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gdisplay.fill(white)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Zombie War", 10,(0,0,0))
        gdisplay.blit(scoretext, (150, 300))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        button()
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    clicked.append(button)
        if button in clicked:
            gdisplay.fill(white)
            return
        pygame.display.update()
        clock.tick(60)

def game(crashed):
    score = 0
    photo = 'hou.png'
    clock = pygame.time.Clock()
    crashed = True
    pop2z = 0
    zombieg = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    h2 = house()
    h1 = house1()
    h = house2()
    h3 = house3()
    houses = pygame.sprite.Group()
    pop = 5
    pop1z = 0
    clicked = []
    hou2 = []
    hou1 = []
    while crashed:
        gdisplay.fill(white)
        allsprites.add(h,h2,h1,h3)
        milliseconds = int(pygame.time.get_ticks())
        seconds = int(pygame.time.get_ticks() / 1000)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                crashed = False
        if 240+100 > mouse[0] > 240 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                clicked.append(h)
        if 425+100 > mouse[0] > 425 and 300+50 > mouse[1] > 300 and h in clicked:
            if click == (1,0,0):
                hou2.append(h2)
        if 50+100 > mouse[0] > 50 and 300+50 > mouse[1] > 300 and h in clicked:
            if click == (1,0,0):
                hou1.append(h1)
                       
        if h in clicked and h2 in hou2:
            if milliseconds % 15 == 0 and pop > 0:
                zomb = zombieupright()
                zombieg.add(zomb)
                allsprites.add(zomb)
                pop -= 1
        if h in clicked and h1 in hou1:
            if milliseconds % 15 == 0 and pop > 0:
                zomb1 = zombieupleft()
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                pop -= 1
        
        
        zombieg.update(pop2z, pop1z)
        allsprites.update(pop2z, pop1z)
        allsprites.draw(gdisplay)
        zombieg.draw(gdisplay)
        for zomb in zombieg:
            allsprites.remove(zomb)
            allsprites.remove(h,h1)
            if pygame.sprite.spritecollide(zomb, allsprites, False):
                zombieg.remove(zomb)
                allsprites.remove(zomb)
                pop2z += 1
                
        for zomb1 in zombieg:
            allsprites.add(h,h1)
            allsprites.remove(h,h2)
            allsprites.remove(zomb1)
            if pygame.sprite.spritecollide(zomb1, allsprites, False):
                zombieg.remove(zomb1)
                allsprites.remove(zomb1)
                pop1z += 1
                
        pygame.display.flip()
    clock.tick(60)
    
def main():
    crashed = True
    start_screen()
    game(crashed)
    pygame.quit()
    exit()
main()

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

class zombieupright(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 1
        self.rect.y -= 3

class zombieupleft(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 1
        self.rect.y -= 3
        
class house(pygame.sprite.Sprite):
    image = None
    def __init__(self, x, y, pop, h, lst):
        super().__init__()
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image = pygame.Surface([130, 50])
        self.image.fill(black)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.pop = pop
        self.h = h
        self.lst = lst
        
    def update(self, pop1):
        if house.image is None:
           house.image = pygame.image.load('hou.png')
           
        if pop1 <= 0:
            self.image = house.image

        elif pop1 > 0 and self.h not in self.lst:
            self.image = pygame.image.load('redhou.png')
            
        elif self.h in self.lst and pop1 > 0:
            self.image = pygame.image.load('redhouselect.png')
        
        elif pop1 <= 0:
            self.image = pygame.image.load('hou.png')
            

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
    count = 0
    photo = 'hou.png'
    pop = 5
    pop1z = 0
    pop3z = -5
    hou2 = []
    hou1 = []
    rightclick = []
    hou2m = []
    clicked = []
    hou1m = []
    hou3 = []
    hou = []
    clock = pygame.time.Clock()
    crashed = True
    pop2z = 0
    zombieg = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    h2 = house(425, 300, pop2z, 'h2', hou2m)
    h = house(240, 550, pop, 'h', clicked)
    h1 = house(50, 300, pop1z, 'h1', hou1m)
    h3 = house(240, 100, pop3z, 'h3', hou2m)
    houses = [h1,h,h2,h3]
    
    while crashed:
        count += 1
        gdisplay.fill(white)
        h.update(pop)
        h1.update(pop1z)
        h2.update(pop2z)
        h3.update(pop3z)
        allsprites.add(h1,h2,h,h3)
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
                clicked.append('h')
        if 50+100 > mouse[0] > 50 and 300+50 > mouse[1] > 300 and 'h' in clicked:
            if click == (1,0,0):
                hou1.append('h1')
        if 50+100 > mouse[0] > 50 and 300+50 > mouse[1] > 300 and 'h' not in clicked:
            if click == (1,0,0):
                hou1m.append('h1')
        if 425+100 > mouse[0] > 425 and 300+50 > mouse[1] > 300 and 'h' in clicked:
            if click == (1,0,0):
                hou2.append('h2')
        
        if 240+100 > mouse[0] > 240 and 100+50 > mouse[1] > 100 and ('h1' in hou1m or 'h2' in hou2m):
            if click == (1,0,0):
                hou3.append('h3')
        
        if 425+100 > mouse[0] > 425 and 300+50 > mouse[1] > 300 and 'h' not in clicked:
            if click == (1,0,0):
                hou2m.append('h2')
                
        if 'h' in clicked and 'h2' in hou2:
            if count % 15 == 0 and pop > 0:
                zomb = zombieupright(350,550)
                zombieg.add(zomb)
                allsprites.add(zomb)
                pop -= 1
        if 'h' in clicked and 'h1' in hou1:
            if count % 15 == 0 and pop > 0:
                zomb1 = zombieupleft(180,550)
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                pop -= 1
        if 'h1' in hou1m and 'h3' in hou3:
            if milliseconds % 15 == 0 and pop1z > 0:
                zomb2 = zombieupright(200,300)
                zombieg.add(zomb2)
                allsprites.add(zomb2)
                pop1z -= 1
        if 'h2' in hou2m and 'h3' in hou3:
            if milliseconds % 15 == 0 and pop2z > 0:
                zomb3 = zombieupleft(360,300)
                zombieg.add(zomb3)
                allsprites.add(zomb3)
                pop2z -= 1
                
        if click == (0,0,1):
            if 'h' in clicked:
                clicked.pop()
            if 'h1' in hou1:
                hou1.pop()
            if 'h2' in hou2:
                hou2.pop()
            if 'h1' in hou1m:
                hou1m.pop()
            if 'h3' in hou3:
                hou3.pop()
            if 'h2' in hou2m:
                hou2m.pop()
        zombieg.update()
        allsprites.draw(gdisplay)
        zombieg.draw(gdisplay)
        for zomb in zombieg:
            allsprites.add(h,h1,h3)
            allsprites.remove(zomb)
            allsprites.remove(h,h1,h3)
            if pygame.sprite.spritecollide(zomb, allsprites, False):
                zombieg.remove(zomb)
                allsprites.remove(zomb)
                pop2z += 1
                     
        for zomb1 in zombieg:
            allsprites.add(h,h1,h3)
            allsprites.remove(h,h2,h3)
            allsprites.remove(zomb1)
            if pygame.sprite.spritecollide(zomb1, allsprites, False):
                zombieg.remove(zomb1)
                allsprites.remove(zomb1)
                pop1z += 1
                
        for zomb2 in zombieg:
            allsprites.add(h,h1,h3)
            allsprites.remove(h,h2,h1)
            allsprites.remove(zomb2)
            if pygame.sprite.spritecollide(zomb2, allsprites, False):
                zombieg.remove(zomb2)
                allsprites.remove(zomb2)
                pop3z += 1
                
        for zomb3 in zombieg:
            allsprites.add(h,h1,h3)
            allsprites.remove(h,h2,h1)
            allsprites.remove(zomb3)
            if pygame.sprite.spritecollide(zomb3, allsprites, False):
                zombieg.remove(zomb3)
                allsprites.remove(zomb3)
                pop3z += 1
        pygame.display.flip()
    clock.tick(60)
    
def main():
    crashed = True
    start_screen()
    game(crashed)
    pygame.quit()
    exit()
main()

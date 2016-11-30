import pygame
import time
import random
import sys
import minigame


pygame.init()
gdisplay = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)
pygame.display.set_caption("Zombie War")

class zombie(pygame.sprite.Sprite):
    image = None
    def __init__(self,x,y, x2, y2, photo):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.photo = photo
        self.x2 = x2
        self.y2 = y2
    def update(self):
        self.rect.x += self.x2
        self.rect.y += self.y2
        if zombie.image is None:
            self.image = pygame.image.load(self.photo)

            
class house(pygame.sprite.Sprite):
    image = None
    def __init__(self, x, y, pop, h, lst, lst2):
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
        self.pop = pop
        self.h = h
        self.lst = lst
        self.lst2 = lst2

        
    def update(self, pop1):
        self.pop1 = pop1
        if house.image is None:
           house.image = pygame.image.load('hou.png')
           
        if pop1 <= 0:
            self.image = house.image

        elif pop1 > 0 and self.h not in self.lst2:
            self.image = pygame.image.load('redhou.png')
            
        elif self.h in self.lst2 and pop1 > 0:
            self.image = pygame.image.load('redhouselect.png')
            
        return self.pop1
    
    def __str__(self):
        return '{} {} {}'.format(self.x, self.y, self.h)
        
def button(text1, text2, text3):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 150+100 > mouse[0] > 150 and 550+50 > mouse[1] > 550:
        pygame.draw.rect(gdisplay, red, (150,550, 130, 60))
       
    else:
        pygame.draw.rect(gdisplay, lightred, (155,550, 120, 50))

    if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
        pygame.draw.rect(gdisplay, red, (395,550, 130, 60))
    else:
        pygame.draw.rect(gdisplay, lightred, (400,550, 120, 50))

    font = pygame.font.Font("freesansbold.ttf",20)
    btext= font.render(text1, 1,(0,0,0))
    gdisplay.blit(btext, (160, 560))

    font2 = pygame.font.Font("freesansbold.ttf",20)
    btext= font2.render(text2, 1,(0,0,0))
    gdisplay.blit(btext, (405, 560))
    
    if text3 != None:
        if 275+100 > mouse[0] > 275 and 600+50 > mouse[1] > 600:
            pygame.draw.rect(gdisplay, red, (270,600, 130, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (275,600, 120, 50))
        font3 = pygame.font.Font("freesansbold.ttf",20)
        btext= font3.render(text3, 1,(0,0,0))
        gdisplay.blit(btext, (280, 610))
    
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
        effect = pygame.mixer.Sound('click.wav')
        button("Start", "Load Game",  None)
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                effect.play()
                gdisplay.fill(white)
                return
        pygame.display.update()
        clock.tick(60)

def level1():
    bg = pygame.image.load("background.png")
    effect = pygame.mixer.Sound('thump.wav')
    score = 0
    count = 0
    pop = 5
    pop1z = 0
    pop2z = 0
    pop3z = -5
    hou = []
    hou2 = []
    clock = pygame.time.Clock()
    crashed = True
    zombieg = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    h2 = house(425, 300, pop2z, 'h2', hou, hou2)
    h = house(240, 550, pop, 'h', hou, hou2)
    h1 = house(50, 300, pop1z, 'h1', hou, hou2)
    h3 = house(240, 100, pop3z, 'h3', hou, hou2)
    houses = [h1,h2,h3]
    houses2 = [h,h1,h2,h3]
    while crashed:
        count += 1
        gdisplay.fill(white)
        gdisplay.blit(bg, (0,0))
        h.update(pop)
        h1.update(pop1z)
        h2.update(pop2z)
        h3.update(pop3z)
        allsprites.add(h1,h2,h,h3)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                crashed = False
        for i in range(len(houses2)):
            stuff = str(houses2[i])
            stuff = stuff.split()
            x = int(stuff[0])
            y = int(stuff[1])
            name = stuff[2]
            i2 = i+1
            if i2 >= 4:
                i2 = 0
            stuff2 = str(houses2[i2])
            stuff2 = stuff2.split()
            x2 = int(stuff[0])
            y2 = int(stuff[1])
            name2 = stuff[2]
        
            if x+100 > mouse[0] > x and y+200 > mouse[1] > y:
                if click == (1,0,0):
                    hou.append(name)
            if x2+100 > mouse[0] > x2 and y2+200 > mouse[1] > y2 and name in hou:
                if click == (1,0,0):
                    hou2.append(name2)
       
     
        if 'h' in hou and 'h2' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb = zombie(350,550, 1, -3,'zombieup.png')
                zombieg.add(zomb)
                allsprites.add(zomb)
                if pop > 1:
                    pop -= 1
        if 'h' in hou and 'h1' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb1 = zombie(180,550, -1, -3, 'zombieup.png')
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                if pop > 1:
                    pop -= 1
        if 'h1' in hou2 and 'h3' in hou:
            if count % 30 == 0 and pop1z > 1:
                zomb2 = zombie(200,300, 1, -3, 'zombieup.png')
                zombieg.add(zomb2)
                allsprites.add(zomb2)
                pop1z -= 1
        if 'h2' in hou2 and 'h3' in hou:
            if count % 30 == 0 and pop2z > 1:
                zomb3 = zombie(360,300, -1, -3, 'zombieup.png')
                zombieg.add(zomb3)
                allsprites.add(zomb3)
                pop2z -= 1
                
        for i in range(len(houses2)):
            if click == (0,0,1):
                stuff = str(houses2[i])
                stuff = stuff.split()
                name = stuff[2]
                if name in hou:
                    hou.remove(name)
                if name in hou2:
                    hou2.remove(name)
   
        if pop > 0:
            if count % 60 == 0:
                pop += 1
        if pop1z > 0:
            if count % 60 == 0:
                pop1z += 1
        if pop2z > 0:
            if count % 60 == 0:
                pop2z += 1
        
        zombieg.update()
        allsprites.draw(gdisplay)
        zombieg.draw(gdisplay)

        for zomb in zombieg:
            for i in houses:
                allsprites.add(h,h1,h2,h3)
                allsprites.remove(h,h1,h2,h3)
                allsprites.remove(zomb)
                allsprites.add(i)
                if pygame.sprite.spritecollide(zomb, allsprites, False):
                    zombieg.remove(zomb)
                    allsprites.remove(zomb)
                    effect.play()
                    if h1 in allsprites:
                        pop1z += 1
                    if h2 in allsprites:
                        pop2z += 1
                    if h3 in allsprites:
                        pop3z += 1
        if pop > 0 and pop1z > 0 and pop2z > 0 and pop3z > 0:
            gdisplay.fill(white)
            return
        
        font = pygame.font.Font("freesansbold.ttf",20)
        btext= font.render(str(pop), 1,(0,0,0))
        gdisplay.blit(btext, (240, 550))
        btext= font.render(str(pop1z), 1,(0,0,0))
        gdisplay.blit(btext, (50,300))
        btext= font.render(str(pop2z), 1,(0,0,0))
        gdisplay.blit(btext, (425,300))
        btext= font.render(str(pop3z), 1,(0,0,0))
        gdisplay.blit(btext, (240,100))
        pygame.display.flip()
        
    clock.tick(60)

def level2():
    bg = pygame.image.load("background.png")
    score = 0
    count = 0
    pop = 5
    pop1z = 0
    pop2z = 0
    pop3z = -5
    pop4z = 0
    hou = []
    hou2 = []
    clock = pygame.time.Clock()
    crashed = True
    zombieg = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()
    h2 = house(260, 260, pop2z, 'h2', hou, hou2)
    h = house(470, 50, pop, 'h', hou, hou2)
    h1 = house(50, 50, pop1z, 'h1', hou, hou2)
    h3 = house(50, 550, pop3z, 'h3', hou, hou2)
    h4 = house(470, 550, pop4z, 'h4', hou, hou2)
    houses = [h1,h2,h3,h4]
    houses2 = [h,h1,h2,h3,h4]
    while crashed:
        count += 1
        gdisplay.fill(white)
        gdisplay.blit(bg, (0,0))
        h.update(pop)
        h1.update(pop1z)
        h2.update(pop2z)
        h3.update(pop3z)
        h4.update(pop4z)
        allsprites.add(h1,h2,h,h3,h4)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                crashed = False
        for i in range(len(houses2)):
            stuff = str(houses2[i])
            stuff = stuff.split()
            x = int(stuff[0])
            y = int(stuff[1])
            name = stuff[2]
            i2 = i+1
            if i2 >= 4:
                i2 = 0
            stuff2 = str(houses2[i2])
            stuff2 = stuff2.split()
            x2 = int(stuff[0])
            y2 = int(stuff[1])
            name2 = stuff[2]
        
            if x+100 > mouse[0] > x and y+200 > mouse[1] > y:
                if click == (1,0,0):
                    hou.append(name)
            if x2+100 > mouse[0] > x2 and y2+200 > mouse[1] > y2 and name in hou:
                if click == (1,0,0):
                    hou2.append(name2)
       
     
        if 'h' in hou and 'h2' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb = zombie(440,70, -1, 3, 'zombie.png')
                zombieg.add(zomb)
                allsprites.add(zomb)
                if pop > 1:
                    pop -= 1
        if 'h' in hou and 'h1' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb1 = zombie(440, 90, -3, 0, 'zombieleft.png')
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                if pop > 1:
                    pop -= 1
        if 'h' in hou and 'h4' in hou2:
            if count % 30 == 0 and pop > 1:
                zomb1 = zombie(470, 130, 0, 3, 'zombie.png')
                zombieg.add(zomb1)
                allsprites.add(zomb1)
                if pop > 1:
                    pop -= 1
                    
        if 'h1' in hou and 'h3' in hou2:
            if count % 30 == 0 and pop1z > 1:
                zomb2 = zombie(60, 160, 0, 3, 'zombie.png')
                zombieg.add(zomb2)
                allsprites.add(zomb2)
                pop1z -= 1
        if 'h2' in hou and 'h3' in hou2:
            if count % 30 == 0 and pop2z > 1:
                zomb3 = zombie(240,350, -1, 3, 'zombie.png')
                zombieg.add(zomb3)
                allsprites.add(zomb3)
                pop2z -= 1
        if 'h2' in hou and 'h4' in hou2:
            if count % 30 == 0 and pop2z > 1:
                zomb3 = zombie(370,355, 1, 3, 'zombie.png')
                zombieg.add(zomb3)
                allsprites.add(zomb3)
                pop2z -= 1
        for i in range(len(houses2)):
            if click == (0,0,1):
                stuff = str(houses2[i])
                stuff = stuff.split()
                name = stuff[2]
                if name in hou:
                    hou.remove(name)
                if name in hou2:
                    hou2.remove(name)
   
        if pop > 0:
            if count % 60 == 0:
                pop += 1
        if pop1z > 0:
            if count % 60 == 0:
                pop1z += 1
        if pop2z > 0:
            if count % 60 == 0:
                pop2z += 1
        font = pygame.font.Font("freesansbold.ttf",20)
        btext= font.render(str(pop), 1,(0,0,0))
        gdisplay.blit(btext, (470, 50))
        btext= font.render(str(pop1z), 1,(0,0,0))
        gdisplay.blit(btext, (50,50))
        btext= font.render(str(pop2z), 1,(0,0,0))
        gdisplay.blit(btext, (260,260))
        btext= font.render(str(pop3z), 1,(0,0,0))
        gdisplay.blit(btext, (50,550))
        btext= font.render(str(pop4z), 1,(0,0,0))
        gdisplay.blit(btext, (470,550))
        zombieg.update()
        allsprites.draw(gdisplay)
        zombieg.draw(gdisplay)

        for zomb in zombieg:
            for i in houses:
                allsprites.add(h,h1,h2,h3, h4)
                allsprites.remove(h,h1,h2,h3,h4)
                allsprites.remove(zomb)
                allsprites.add(i)
                if pygame.sprite.spritecollide(zomb, allsprites, False):
                    zombieg.remove(zomb)
                    allsprites.remove(zomb)
                    if h1 in allsprites:
                        pop1z += 1
                    if h2 in allsprites:
                        pop2z += 1
                    if h3 in allsprites:
                        pop3z += 1
                    if h4 in allsprites:
                        pop4z += 1
        if pop > 0 and pop1z > 0 and pop2z > 0 and pop3z > 0 and pop4z > 0:
            gdisplay.fill(white)
            return
        pygame.display.flip()
    clock.tick(60)
    
def btwlevel():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        effect = pygame.mixer.Sound('click.wav')
        gdisplay.fill(white)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Level Complete", 10,(0,0,0))
        gdisplay.blit(scoretext, (100, 300))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        button("Next Level", "Exit", "Minigame")
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                effect.play()
                gdisplay.fill(white)
                return
        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                effect.play()
                pygame.quit()
                sys.exit()
        if 275+100 > mouse[0] > 275 and 600+50 > mouse[1] > 600:
            if click == (1,0,0):
                effect.play()
                minigame.playminigame()
                return
        pygame.display.update()
        clock.tick(60)

def main():
    music = pygame.mixer.Sound('star.wav')
    music.play(loops=-1)
    start_screen()
    level1()
    btwlevel()
    level2()
    btwlevel()
    pygame.quit()
    exit()
main()

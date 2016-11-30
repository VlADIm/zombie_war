import pygame
import random
import sys

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([20, 30])
    
        self.rect = self.image.get_rect()
        
    
            
    def update(self):
        pos = pygame.mouse.get_pos()
 
        self.rect.x = pos[0]
        self.rect.y = 550

    def set_image(self, filename = None):
        if (filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
    
class Apple(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([1, 40])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        if Apple.image is None:
            Apple.image = pygame.image.load('brain.png')
        self.image = Apple.image
    def update(self):
        self.rect.y += 10

def texts(score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score), 1,(0,0,0))
   gdisplay.blit(scoretext, (10, 10))


pygame.init()
gdisplay = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)
pygame.display.set_caption("Zombie War")


class button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (150,550, 130, 60))          
        else:
            pygame.draw.rect(gdisplay, lightred, (155,550, 120, 50))

        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (395,550, 130, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (400,550, 120, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Play Again", 1,(0,0,0))
        gdisplay.blit(btext, (160, 560))

        font3 = pygame.font.Font("freesansbold.ttf",20)
        btext= font3.render("Next Level", 1,(0,0,0))
        gdisplay.blit(btext, (400, 560))
        
all_sprites_list = pygame.sprite.Group()
apple_list = pygame.sprite.Group()
yel_list = pygame.sprite.Group()
black_list = pygame.sprite.Group()

clock = pygame.time.Clock()
player = Player()
all_sprites_list.add(player)
player.set_image('guy.png')

pygame.time.set_timer(pygame.USEREVENT, 1000)
def pregame():
    running = True
    font=pygame.font.Font(None,70)
    scoretext=font.render("Time for a minigame!", 10,(0,0,0))
    font=pygame.font.Font(None,40)
    scoretext1=font.render("Collect the brains", 10,(0,0,0))
    font=pygame.font.Font(None,40)
    scoretext2=font.render("Before the time runs out", 10,(0,0,0))
    font=pygame.font.Font("freesansbold.ttf",20)
    scoretext3=font.render("Play", 1,(0,0,0))
    while running:
        gdisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gdisplay.blit(scoretext, (90, 300))
        gdisplay.blit(scoretext1, (200, 400))
        gdisplay.blit(scoretext2, (170, 450))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 250+100 > mouse[0] > 250 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (245,550, 130, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (250,550, 120, 50))
        if 250+100 > mouse[0] > 250 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                return
        gdisplay.blit(scoretext3,  (260, 550))
        pygame.display.update()
        clock.tick(60)
        
def game(crashed):
    bg = pygame.image.load("background.png")
    score = 0
    count = 0
    counter, text = 10, '10'.rjust(3)
    crashed = True
    font = pygame.font.Font("freesansbold.ttf",30)
    while crashed:
        count += 1
        new_list = pygame.sprite.Group()
        new_list.add(player)
        gdisplay.fill(white)
        gdisplay.blit(bg, (0,0))
        seconds = pygame.time.get_ticks()
        seconds = str(seconds)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                crashed = False
        
            if event.type == pygame.USEREVENT: 
                counter -= 1
                if counter >= 0:
                    text = str(counter).rjust(3) 
            if event.type == pygame.QUIT: break
        
        
        if count % 25 == 0:
                apple = Apple()
                
                apple.rect.x = random.randrange(590)
                apple.rect.y = 0
               
                all_sprites_list.add(apple)
                apple_list.add(apple)
       
        all_sprites_list.update()
        all_sprites_list.draw(gdisplay)
        for apple in apple_list:
            if pygame.sprite.spritecollide(apple, new_list, True):
                apple_list.remove(apple)
                all_sprites_list.remove(apple)
                all_sprites_list.add(player)
                score += 1
    
        gdisplay.blit(font.render(text, True, (0, 0, 0)), (290, 48))
        
        if counter == 0:
            gameover(crashed, score)
            return
      
        texts(score)
        pygame.display.flip()
    
    clock.tick(100)
    
def gameover(crashed, score):
    clicked = []
    running = True
    while running:
        gdisplay.fill(white)
        button()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                running = False
        font=pygame.font.Font(None,90)
        scoretext=font.render("Time's Up", 10,(0,0,0))
        gdisplay.blit(scoretext, (150,300))
        font=pygame.font.Font(None,70)
        scoretext=font.render("Your Score:" + str(score), 10,(0,0,0))
        gdisplay.blit(scoretext, (150,400))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    game(crashed)
        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    return
        
            
        pygame.display.update()



def playminigame():
    pregame()
    crashed = True
    game(crashed)





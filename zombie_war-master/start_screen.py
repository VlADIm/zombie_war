import pygame
import button
import load_save_screen
import time
import random
import sys
import minigame
import game

pygame.init()


gdisplay = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)
pygame.display.set_caption("Zombie War")

class start_screen(pygame.sprite.Sprite):

    def __init__(self):
        while True:
            for event in pygame.event.get():
                self.button1 = button.Button("New Game", 425, 350)
                self.button2 = button.Button("Load Game", 625, 350)

                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                else:
                    gdisplay.fill(white)
                    font=pygame.font.Font(None,90)
                    scoretext=font.render("Zombie War", 10, black)
                    gdisplay.blit(scoretext, (425, 200))

                    self.buttons(self.button1)
                    self.buttons(self.button2)
                    effect = pygame.mixer.Sound('click.wav')

                    if(self.button1.next() == True):
                        effect.play()
                        gdisplay.fill(white)
                        name = input("Please enter a four character save name: ")
                        new_save = {"strength": 1, "r_rate": 1, "speed": 1, "level": 1}
                        name = game.Game(name)
                        name.saveGame(new_save)
                        game_data = game.game.Game()
                        # new screen here

                    if(self.button2.next() == True):
                        effect.play()
                        gdisplay.fill(white)
                        load_save_screen.load_save_screen()

                    pygame.display.flip()
    def buttons(self, a_button):

        if(a_button.inside() == True):
            pygame.draw.rect(gdisplay, red, (a_button.x_coor - 15, a_button.y_coor - 10, 140, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (a_button.x_coor - 10, a_button.y_coor - 10, 130, 50))

        font = pygame.font.Font("freesansbold.ttf",20)
        some_text= font.render(a_button.text, 1, black)
        gdisplay.blit(some_text, (a_button.x_coor, a_button.y_coor))


start_screen()

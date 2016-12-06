import pygame
import button
import game
import sys


pygame.init()


gdisplay = pygame.display.set_mode((1200,600))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)

class load_save_screen(pygame.sprite.Sprite):

    def __init__(self):
        while True:
            for event in pygame.event.get():

                all_saves = game.Game('all')
                saves = all_saves.loadGame()

                if(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

                else:
                    gdisplay.fill(white)
                    font=pygame.font.Font(None,90)
                    scoretext=font.render("Saved Games", 10, black)
                    gdisplay.blit(scoretext, (100, 100))

                    x_coordinate = 125
                    y_coordinate = 250
                    for i in saves:
                        if x_coordinate > 550:
                            x_coordinate = 125
                            y_coordinate = 350
                        self.button = button.Button(i, x_coordinate, y_coordinate)
                        self.buttons(self.button)
                        x_coordinate += 150

                        effect = pygame.mixer.Sound('click.wav')

                        if(self.button.next() == True):
                            selected_save = game.Game(self.button.text)
                            game_data = selected_save.loadGame()

                            effect.play()
                            gdisplay.fill(white)

                            # new screen here

                    pygame.display.flip()

    def buttons(self, a_button):

        if(a_button.inside() == True):
            pygame.draw.rect(gdisplay, red, (a_button.x_coor - 45, a_button.y_coor - 10, 140, 60))
        else:
            pygame.draw.rect(gdisplay, lightred, (a_button.x_coor - 40, a_button.y_coor - 10, 130, 50))

        font = pygame.font.Font("freesansbold.ttf",20)
        some_text= font.render(a_button.text, 1, black)
        gdisplay.blit(some_text, (a_button.x_coor, a_button.y_coor))

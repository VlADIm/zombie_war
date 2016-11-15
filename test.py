import house
import sys
import pygame
# def main():
#
#     vlad = game.Game("evan")
#     # print(vlad.loadGame())
#     save = {"speed":1,"strength":1,"r_rate":2}
#     vlad.saveGame(save)
#     print("done")
#     print(vlad.loadGame())
pygame.init()
white = (255,255,255)
def main():
    clock = pygame.time.Clock()
    gdisplay = pygame.display.set_mode((600,800))
    allsprites = pygame.sprite.Group()

    running = True
    while running:
        gdisplay.fill(white)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                running = False
        justin = house.House(200, 200, False, 5, None)
        justin.placeHouse()
        justin.checkClicked()
        justin.makeBorder()
        allsprites.add(justin)

        allsprites.update()
        allsprites.draw(gdisplay)

        pygame.display.update()
    clock.tick(60)
main()

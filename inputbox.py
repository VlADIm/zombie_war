import pygame, pygame.font, pygame.event, pygame.draw, string, sys
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  bg = pygame.image.load("background.png")
  screen.blit(bg, (0,0))
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 150,
                    (screen.get_height() / 2) - 40,
                    350,80), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 152,
                    (screen.get_height() / 2) - 42,
                    350,80), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 150, (screen.get_height() / 2) - 40))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + "".join(current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + "".join(current_string))
  return "".join(current_string)

def main():
  screen = pygame.display.set_mode((600,800))
  print (ask(screen, "Name") + " was entered")

if __name__ == '__main__': main()

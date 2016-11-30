import pygame

pygame.init()

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

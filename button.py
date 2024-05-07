import pygame

class Button:

    def __init__(self, x, y,pay):
        self.x = x
        self.y = y
        self.pay = pay
        self.image = pygame.image.load("img.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.045, self.image_size[1] * 0.068)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.045, self.image_size[1]*0.068)
        self.image_size = self.image.get_size()
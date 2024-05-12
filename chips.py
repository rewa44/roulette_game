import pygame

class Chip:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.2
        self.image = pygame.image.load("red_chip.jpg")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*park, self.image_size[1]*park)
        self.image_size = self.image.get_size()


class Chip2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.2
        self.image = pygame.image.load("blue_chip.jpg")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * park, self.image_size[1] * park)
        self.image_size = self.image.get_size()

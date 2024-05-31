import pygame

class Wheel:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.5
        self.image = pygame.image.load("samtp.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*park, self.image_size[1]*park)
        self.image_size = self.image.get_size()

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.7
        self.image = pygame.image.load("download.jpg")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*park, self.image_size[1]*park)
        self.image_size = self.image.get_size()
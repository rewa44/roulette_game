import pygame

class Rod:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fist = []
        self.pay = 3
        self.image = pygame.image.load("img.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.05, self.image_size[1] * 0.068)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.05, self.image_size[1]*0.068)
        self.image_size = self.image.get_size()

class Button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pay = 1
        self.image = pygame.image.load("img.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.045, self.image_size[1] * 0.068)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.045, self.image_size[1]*0.068)
        self.image_size = self.image.get_size()

class Roulette:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("roulette.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.3, self.image_size[1] * 1.3)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()

class Evdd:

    def __init__(self, x, y, pay):
        self.x = x
        self.y = y
        self.pay = pay
        self.fist = []
        self.image = pygame.image.load("img.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * (0.195/2), self.image_size[1] * 0.05)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*(0.195/2), self.image_size[1]*0.05)
        self.image_size = self.image.get_size()
class Doz:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pay = 3
        self.fist = []
        self.image = pygame.image.load("img.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.195, self.image_size[1] * 0.05)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.195, self.image_size[1]*0.05)
        self.image_size = self.image.get_size()

class Spin:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.5
        self.image = pygame.image.load("spin.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*park, self.image_size[1]*park)
        self.image_size = self.image.get_size()

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

class Chip3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        park = 0.7
        self.image = pygame.image.load("clementine.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * park, self.image_size[1] * park)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * park, self.image_size[1] * park)
        self.image_size = self.image.get_size()

class City:
    def __init__(self):
        self.kist = []

import pygame


class Square1:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('m1.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self, x, y):
        self.screen.blit(self.image, (x, y))

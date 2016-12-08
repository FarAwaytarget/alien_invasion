
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """docstring for Alien."""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.rect = screen
        self.ai_settings = ai_settings
        #load alien image and set attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #set every alien in screen left the up
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #store alien accurate
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move right'''
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

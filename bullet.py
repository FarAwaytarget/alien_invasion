import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # creat a rect bullet
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.ship_speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """up moving bullet"""
        self.y -= self.ship_speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """fill bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

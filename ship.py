import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        # initialization place the ship screen
        self.screen = screen
        self.ai_settings = ai_settings
        # load image and obtain rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # place the ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # in ship store float
        self.center = float(self.rect.centerx)
        self.down_up = float(self.rect.top)

        self.moving_down = False
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # draw place the ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < 600:
            print(self.rect.top, self.rect.bottom)
            self.down_up += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top+30 :
            self.down_up -= self.ai_settings.ship_speed_factor
            print(self.rect.bottom)
        self.rect.centerx = self.center
        self.rect.bottom = self.down_up

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.down_up = self.screen_rect.bottom
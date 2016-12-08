import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
#初始化，并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((
            ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # create aliens Group
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #again game main loop
    while True:
        #moitoring keyboard and mouse time
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        #delete not visible bullets
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()

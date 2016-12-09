import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf

def run_game():
#初始化，并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((
            ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
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
        if stats.game_active:
            ship.update()
            bullets.update()
        #delete not visible bullets
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()

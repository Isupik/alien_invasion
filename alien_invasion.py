import sys
import pygame
from pygame.sprite import Group

from conf.settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # ((2560, 1440))
    pygame.display.set_caption('Alien Invasion')
    button = Button(screen, 'Играть')
    stats = GameStats(ai_settings)  # Создание экземпляра для хранения игровой статистики
    ship = Ship(ai_settings=ai_settings, screen=screen)
    bullets = Group()
    alien = Alien(ai_settings=ai_settings, screen=screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, stats, button, ship, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, button)

run_game()

import sys
import pygame
from pygame.sprite import Group

from conf.settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    Начинаем игру, задаем размеры экрана.
    Назначаем цвет фона.
    Запуск основного цикла игры, отслеживание событий и отображение последнего отрисованного экрана.
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # ((2560, 1440))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings=ai_settings, screen=screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

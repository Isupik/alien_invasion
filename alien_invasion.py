import sys
import pygame

from conf.settings import Settings

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)

        pygame.display.flip()


run_game()

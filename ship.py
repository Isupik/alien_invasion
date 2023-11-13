import pygame

from conf.settings import Settings


class Ship():
    def __init__(self, screen):
        """Инициализируем корабль и задает его начальную позицию"""
        self.screen = screen
        ai_settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'), (ai_settings.ship_width, ai_settings.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
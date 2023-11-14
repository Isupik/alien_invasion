import pygame

from conf.settings import Settings


class Ship():
    def __init__(self, ai_settings, screen):
        """Инициализируем корабль и задает его начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'),
                                            (ai_settings.ship_width, ai_settings.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

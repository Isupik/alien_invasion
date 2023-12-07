import sys
import pygame
from bullet import Bullet
from alien import Alien
"""Обрабатывается нажатие клавиш и событий мышки"""


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_evehts(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def check_keyup_evehts(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()


    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

# def create_fleet(ai_settings, screen, aliens):
#     alien = Alien(ai_settings, screen)
#     available_space_x = ai_settings.screen_width - 2 * ai_settings.alien_width
#     number_aliens_x = int(available_space_x / (2 * ai_settings.alien_width))

    # for alien_number in range(number_aliens_x):
    #     alien = Alien(ai_settings, screen)
    #     alien.x = ai_settings.alien_width + 2 * ai_settings.alien_width * alien_number
    #     alien.rect.x = alien.x
    #     aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляем кол-во пришельцев в ряду"""
    available_space_x = ai_settings.screen_width - 2 * ai_settings.alien_width
    number_aliens_x = int(available_space_x / (2 * ai_settings.alien_width))
    return number_aliens_x

def create_allien(ai_settings, screen, aliens, alien_number, row_number):
    """Создание пришельца и размещение его в ряду"""
    alien = Alien(ai_settings, screen)
    # alien_width = alien.rect.width
    alien.x = ai_settings.alien_width + 2 * ai_settings.alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев
    Создание пришельца и вычисление кол-ва пришельцев в ряду"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Создание первого ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_allien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет кол-во рядовб перемещающихся на экране"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

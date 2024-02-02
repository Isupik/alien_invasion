import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep




def check_events(ai_settings, screen, stats, button, ship, bullets):
    """Обрабатывается нажатие клавиш и событий мышки"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, button)
        elif event.type == pygame.KEYUP:
            check_keyup_evehts(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, button, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, button):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        stats.game_active = False
        button.prep_msg("Продолжить")


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_evehts(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Кнопка Play отображается в том случае, если игра неактивна
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Обновляет позиции пуль и удаляет старые пули"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Обработка коллизий пуль с пришельцами
    Удаление пуль и пришельцев, участвующих в коллизиях"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


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
    """Определяет кол-во рядов перемещающихся на экране"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Проверяет, достиг ли флот края экрана, после чего обновляет позиции всех пришельцев"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Проверка коллизий "пришелец-корабль"
    if pygame.sprite.spritecollideany(ship, aliens):
        # print("Корабль попал!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижения пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцем"""
    if stats.ships_left > 0:

        # Уменьшение ship_left
        stats.ships_left -= 1

        # Очистка списков пришельцев и пуль
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение коробля в центре
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Пауза
        sleep(1)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Проверяет, добрались ли пришельцы до нижнего края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что при столкновении с кораблем
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def check_play_button(stats, play_button, mouse_x, mouse_y):
    """"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
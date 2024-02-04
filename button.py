import pygame.font

import button_types

TYPE_TO_NAME = {
    button_types.button_type.PLAY: "Играть",
    button_types.button_type.RESUME: "Продолжить",
    button_types.button_type.EXIT: "Выход",
}


class Button():

    def __init__(self, screen, msg=None, type=None):
        """Инициализирует атрибуты кнопки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.type = type
        self.visability = False

        # Назначение размеров и свойств кнопок
        self.width, self.height = 250, 50
        self.button_color = (50, 205, 50)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Простроение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def get_list_buttons(self):
        global TYPE_TO_NAME
        buttons = []

        for button_type in button_types.button_type:
            buttons.append(Button(self.screen, msg=TYPE_TO_NAME[button_type], type=button_type))
            if button_type == button_types.button_type.PLAY:
                buttons[-1].visability = True

        return buttons

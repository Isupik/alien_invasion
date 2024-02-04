class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует статистические настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (70, 130, 180)
        self.ship_width = 70
        self.ship_height = 70
        self.ship_speed_factor = 5
        self.ship_limit = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = [(255, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.bullets_allowed = 5
        self.alien_width = 70
        self.alien_height = 70
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 100
        self.fleet_direction = 1  # движение вправо
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

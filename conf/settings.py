class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        self.screen_width = 2560
        self.screen_height = 1300
        self.bg_color = (70, 130, 180)
        self.ship_width = 70
        self.ship_height = 70
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = [(255, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.bullets_allowed = 5
        self.alien_width = 70
        self.alien_height = 70

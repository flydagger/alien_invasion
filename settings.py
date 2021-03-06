class Settings:
    """
    Store all settings for Alien Invasion
    """
    def __init__(self):
        """initialize game static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        # self.bullet_width = 600  # for testing
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # game speed factor
        self.speedup_scale = 1.1

        # the speed of increasing alien point
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction==1 means moving right, -1 means moving left
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        """increase game speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


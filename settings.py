class Settings():
    """docstring for Settings."""
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.ship_speed_factor = 40
        self.ship_limit = 1
        self.bg_color = (230,230,230)
        #setting bullet
        self.bullet_speed_factor = 20
        self.bullet_width = 1000
        self.bullet_height = 5
        self.bullet_color = 60,60,60
        self.bullet_allowed = 20
        #alien  setting
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 30
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialization_dynamic_settings()
        #score

    def initialization_dynamic_settings(self):
        self.ship_speed_factor = 30
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1
        #score
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

class Settings():
    """docstring for Settings."""
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.ship_speed_factor = 4
        self.bg_color = (230,230,230)
        #setting bullet
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        #alien  setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

class Settings():
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initiate settings of game."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
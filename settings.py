class Settings():
    """Class for saving all settings Alien Invasion game."""

    def __init__(self):
        """Initiates settings of game."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
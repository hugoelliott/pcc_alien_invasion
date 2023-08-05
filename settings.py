class Settings:
    """A class to store all settings for Alien Invastion"""

    def __init__(self):
        """Initiallised the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200,230,230)
        # Ship settings
        self.ship_speed = 1.5
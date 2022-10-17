class PanelSettings:
    """Stores all game penal/frame settings"""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.game_title = 'Alien Invasion'


class AISettings:
    """Stores all AI settings"""

    def __init__(self):
        """Initialize the AI settings"""

        # the settings of ship
        self.ship_speed = 1.0
        self.ship_init_pos = None  # set the initial position of the ship. If None, set bottom-center
        self.ship_size = [60, 48]
        self.ship_limit = 3  # how many ship can be used for the game

        # the settings of bullet
        self.bullet_pos = None
        self.bullet_speed = 1
        self.bullet_size = [3, 15]
        self.bullet_allowed = 3  # controls the shoot frequency
        self.bullet_color = (60, 60, 60)

        # the settings of alien
        self.alien_img_path = 'images/alien.bmp'
        self.alien_num = 8  # this number is only the initial alien number. The actual number of aliens will be calculated through AlienFleet class
        self.alien_size = [60, 58]
        self.alien_init_pos = None
        self.alien_speed = [0.1, 10.0]  # speed on x and y axis

        # the settings of alien fleet
        self.fleet_speed = [0.05, 10.0]


class Settings:
    """Stores all penal and AI settings"""

    def __init__(self):
        """Initialize the settings"""
        self.panel_settings = PanelSettings()
        self.ai_settings = AISettings()
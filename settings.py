class PenalSettings:
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
        self.ship_pos = None  # set the initial position of the ship. If None, set bottom-center

        # the settings of bullet
        self.bullet_pos = None
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_allowed = 3  # controls the shoot frequency
        self.bullet_color = (60, 60, 60)

        # the settings of alien

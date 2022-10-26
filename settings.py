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

    def __init__(self, absolute_path=''):
        """Initialize the AI settings"""

        # the settings of ship
        self.ship_img_path = absolute_path + 'images/ship.bmp'
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
        self.alien_img_path = absolute_path + 'images/alien.bmp'
        self.alien_num = 8  # this number is only the initial alien number. The actual number of aliens will be calculated through AlienFleet class
        self.alien_size = [60, 58]
        self.alien_init_pos = None
        self.alien_speed = [0.1, 10.0]  # speed on x and y axis

        # the settings of alien fleet
        self.fleet_speed = [0.05, 10.0]


class StateSettings:
    """Stores all status settings"""

    def __init__(self, absolute_path=''):
        # the settings of the player status
        self.heart_img_path = absolute_path + 'images/heart.bmp'
        self.heart_size = [20, 20]
        self.heart_init_pos = [10, 10]

        # the settings of the text of status
        self.text_score = {
            'font_type': 'Arial',
            'font_size': 30,
            'font_color': (0, 0, 0),
            'position': None,  # if None, the title will be set to the center position, else assign to (x, y)
        }


class GUISettings:
    """Stores all GUI settings"""

    def __init__(self):
        self.title = {
            'font_type': 'Arial',
            'font_size': 60,
            'bg_color': (0, 0, 0),
            'position': None,  # if None, the title will be set to the center position, else assign to (x, y)
        }

        # the button settings only stores the general style settings of the button
        self.button = {
            'font_type': 'Arial',
            'font_size': 40,
            'font_color': (255, 255, 255),
            'ft_color': (150, 150, 150),
            'bg_color': (100, 100, 100),
        }

        self.game_stage = 0  # 0: title, 1: play, 2: gameover


class Settings:
    """Stores all penal and AI settings"""

    def __init__(self):
        """Initialize the settings"""
        self.absolate_path = 'E:/Projects/alien_invasion/'
        self.panel_settings = PanelSettings()
        self.ai_settings = AISettings(self.absolate_path)
        self.state_settings = StateSettings(self.absolate_path)
        self.GUI_settings = GUISettings()

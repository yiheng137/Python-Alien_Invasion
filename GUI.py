import pygame
from panels import title_panel, play_panel, game_over_pannel


class GameGUI:
    """This class draw different GUIs (start, game play, game over, score) for the game play"""

    def __init__(self, settings, screen, game_states):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.GUI_settings = settings.GUI_settings
        self.game_states = game_states

        # Create the title panel
        self.title_panel = title_panel.TitlePanel(settings, screen)

        # Create the game play panel
        self.game_panel = play_panel.PlayPanel(settings, screen, game_states)

        # Create the game over panel
        self.game_ovel_panel = game_over_pannel.GameOverPanel(settings, screen, game_states)

    def show_title_panel(self):
        """Show the start panel"""
        self.title_panel.show()
        pygame.display.update()

    def show_play_panel(self):
        self.game_panel.show()
        pygame.display.update()

    def show_game_over_panel(self):
        """Show the game over panel"""
        self.game_ovel_panel.show()
        pygame.display.update()

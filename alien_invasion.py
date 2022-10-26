import sys

import pygame
import game_stats
import GUI


class MainGame:
    def __init__(self, settings):
        self.settings = settings
        self.panel_settings = settings.panel_settings
        self.ai_settings = settings.ai_settings
        self.state_settings = settings.state_settings
        self.GUI_settings = settings.GUI_settings

        pygame.init()
        self.screen = pygame.display.set_mode((self.panel_settings.screen_width, self.panel_settings.screen_height))
        pygame.display.set_caption(self.settings.panel_settings.game_title)

        # Create an instance to store game statistics.
        self.game_states = game_stats.GameStats(self.settings, self.screen)

        # Create game GUI
        self.GUI = GUI.GameGUI(self.settings, self.screen, self.game_states)

    def start(self):
        '''Run the game'''
        while True:
            # Watch for keyboard and mouse events.
            if self.GUI_settings.game_stage == 0:  # show the title panel
                self.GUI.show_title_panel()
            elif self.GUI_settings.game_stage == 1:
                self.GUI.show_play_panel()
            elif self.GUI_settings.game_stage == 2:
                self.GUI.show_game_over_panel()
            else:
                pass

            self.__check_events()

    def __check_events(self):
        """Respond to keypresses and mouse events to different panels."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if click the right-top 'x' button, quit the game
                sys.exit()
            elif self.GUI_settings.game_stage == 1:
                self.GUI.game_panel.events(event)
            elif self.GUI_settings.game_stage == 2:
                self.GUI.game_ovel_panel.events(event)

import sys

import pygame
import button


class TitlePanel:
    """
    This class draws the title panel of the game
    """

    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.GUI_settings = settings.GUI_settings

        # Create a title panel to the game
        title_info = self.GUI_settings.title
        self.title_font = pygame.font.SysFont(title_info['font_type'], title_info['font_size'])
        self.title_text = self.title_font.render('Alien Invasion', True, title_info['bg_color'])
        self.title_rect = self.title_text.get_rect()

        self.buttons = pygame.sprite.Group()

        # Create a 'Start' button
        size = (120, 40)
        x = self.settings.panel_settings.screen_width // 2 - size[0] - 20  # include an interval
        y = self.settings.panel_settings.screen_height // 2 + 50
        self.__add_button('Start', (x, y), size)

        # Create a 'Quit' button
        x = settings.panel_settings.screen_width // 2 + 20
        self.__add_button('Quit', (x, y), size)

        if title_info['position']:
            self.title_rect.center = title_info['position']
        else:
            self.title_rect.center = self.screen_rect.center
            self.title_rect.centery = self.screen_rect.centery * 0.7

    def __add_button(self, title, position, size):
        new_button = button.Button(self.screen, self.GUI_settings, title)
        new_button.set_rect(position, size)
        self.buttons.add(new_button)

    def show(self):
        """Show the start panel"""
        self.screen.fill(self.settings.panel_settings.bg_color)
        self.screen.blit(self.title_text, self.title_rect)
        self.buttons.update()
        for button in self.buttons.sprites():
            # mouse event to the button
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    button.cur_button_color = button.bg_color
                    button.pressed = True
                else:
                    button.cur_button_color = button.ft_color
                    if button.pressed:
                        # button events
                        self.__events(button)
                        button.pressed = False
            else:
                button.cur_button_color = button.bg_color

            button.draw()

    def __events(self, button):
        """
        implement the button events
        :param button: the button class
        :return: None
        """
        if button.label == 'Start':
            self.GUI_settings.game_stage = 1
        elif button.label == 'Quit':
            sys.exit()

import pygame


class Button(pygame.sprite.Sprite):
    """Create buttons of the game"""

    def __init__(self, screen, GUI_settings, title=''):
        super().__init__()
        self.screen = screen
        self.GUI_settings = GUI_settings
        self.button_info = GUI_settings.button

        if self.button_info['ft_color']:  # stores the front and background colors
            self.ft_color = self.button_info['ft_color']
        else:
            self.ft_color = (170, 170, 170)

        if self.button_info['bg_color']:
            self.bg_color = self.button_info['bg_color']
        else:
            self.bg_color = (100, 100, 100)

        self.font = pygame.font.SysFont(self.button_info['font_type'], self.button_info['font_size'])
        self.text_render = self.font.render(title, True, self.button_info['font_color'])
        self.title_rect = self.text_render.get_rect()
        self.label = title

        # self.image = pygame.image.load(self.button_info['img_path'])

        self.rect = None
        self.pressed = False

        self.cur_button_color = self.bg_color

    def set_rect(self, position, size):
        """
        Set the left-top position and size of the button
        :param position: left-top position of the button. Type: tuple
        :param size: the width and height of the button. Type: tuple
        :return: None
        """
        self.size = size
        self.pos = position
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.title_rect.center = self.rect.center

    def draw(self):
        """draw the button on the screen"""
        pygame.draw.line(self.screen, (150, 150, 150), self.pos, [self.pos[0] + self.size[0], self.pos[1]], 5)
        pygame.draw.line(self.screen, (150, 150, 150), [self.pos[0], self.pos[1] - 2], [self.pos[0], self.pos[1] + self.size[1]], 5)
        pygame.draw.line(self.screen, (50, 50, 50), (self.pos[0], self.pos[1] + self.size[1]), (self.pos[0] + self.size[0], self.pos[1] + self.size[1]), 5)
        pygame.draw.line(self.screen, (50, 50, 50), (self.pos[0] + self.size[0], self.pos[1] + self.size[1]), [self.pos[0] + self.size[0], self.pos[1]], 5)
        pygame.draw.rect(self.screen, self.cur_button_color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        self.screen.blit(self.text_render, self.title_rect)  # draw the text of the button

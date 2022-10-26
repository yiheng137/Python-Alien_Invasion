import pygame
import json
from functools import cmp_to_key


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, settings, screen):
        """Initialize statistics."""
        self.ai_settings = settings.ai_settings
        self.state_settings = settings.state_settings
        self.screen = screen

        self.ships_left = 0
        self.score = 0

        self.reset_stats()
        # Create heart img
        ori_img = pygame.image.load(self.state_settings.heart_img_path)
        self.heart = pygame.transform.scale(ori_img, self.state_settings.heart_size)

        # Create score text
        text_settings = self.state_settings.text_score
        self.font = pygame.font.SysFont(text_settings['font_type'], text_settings['font_size'])
        self.text_render = self.font.render('Score: ' + str(self.score), True, text_settings['font_color'])
        self.text_rect = self.text_render.get_rect()
        self.text_rect.topright = self.screen.get_rect().topright

        # load the rank
        self.rank = []
        self.__load_rank()

        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

    def update_rank(self):
        """
        Add the new record into the rank list and sort according to the score. Choose the top-3 records and save into file
        :return: None
        """
        self.rank.append(['No Name', self.score])

        def cmp(a, b):
            return a[1] - b[1]

        self.rank.sort(key=cmp_to_key(cmp), reverse=True)
        self.rank = self.rank[:3]  # only store top three records
        self.__save_rank()

    def __load_rank(self):
        """
        Load the rank information from the file
        :return: None
        """
        with open('rank.json', 'r') as f:
            self.rank = json.load(f)
            for i in range(len(self.rank)):
                self.rank[i][1] = int(self.rank[i][1])

    def __save_rank(self):
        """
        Save the rank to the file
        :return: None
        """
        with open('rank.json', 'w') as f:
            json.dump(self.rank, f)

    def display(self):
        """Display the healthy and scores on the screen"""
        for i in range(self.ships_left):
            self.screen.blit(self.heart, (self.state_settings.heart_init_pos[0],
                                          self.state_settings.heart_init_pos[1] + 10 + self.state_settings.heart_size[
                                              1] * i))

        """Display the score"""
        self.text_render = self.font.render('Score: ' + str(self.score), True, self.state_settings.text_score['font_color'])
        self.text_rect = self.text_render.get_rect()
        self.text_rect.topright = self.screen.get_rect().topright
        self.screen.blit(self.text_render, self.text_rect)
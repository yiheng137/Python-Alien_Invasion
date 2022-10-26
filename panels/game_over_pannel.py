import pygame


class GameOverPanel:
    """
    Display the game over panel
    """

    def __init__(self, settings, screen, game_stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.GUI_settings = settings.GUI_settings
        self.game_stats = game_stats

        # Create 'Game Over' text
        game_over_font = pygame.font.SysFont('Arial', 50)
        self.text_game_over = game_over_font.render('Game Over', True, (0, 0, 0))
        self.text_rect = self.text_game_over.get_rect()
        self.text_rect.center = (self.screen.get_rect().centerx, self.screen.get_rect().centery * 0.5)

        # Create rank table
        self.text_ranks = []
        self.update_rank()

        # Message 'Press any key to continue'
        message_font = pygame.font.SysFont('Arial', 20)
        self.text_message = message_font.render('Press any key to continue', True, (0, 0, 0))
        self.text_message_rect = self.text_message.get_rect()
        self.text_message_rect.center = (self.screen.get_rect().centerx, self.screen.get_rect().centery * 1.85)

    def update_rank(self):
        ranks = self.game_stats.rank
        x1 = self.screen.get_rect().centerx - 100
        x2 = self.screen.get_rect().centerx + 100
        y = self.screen.get_rect().centery
        self.text_ranks = []

        rank_font = pygame.font.SysFont('Arial', 30)
        for i in range(len(ranks)):
            # add name
            self.text_ranks.append(self.__get_text(rank_font, ranks[i][0], x1, y + i * 40))

            # add score
            self.text_ranks.append(self.__get_text(rank_font, str(ranks[i][1]), x2, y + i * 40))

    def __get_text(self, font, text, x, y):
        text_font = font.render(text, True, (0, 0, 0))
        text_rect = text_font.get_rect()
        text_rect.center = (x, y)
        return [text_font, text_rect]

    def show(self):
        """
        Show the panel of game over
        :return:
        """
        self.screen.fill(self.settings.panel_settings.bg_color)
        self.screen.blit(self.text_game_over, self.text_rect)
        self.screen.blit(self.text_message, self.text_message_rect)

        # Show rank
        self.update_rank()
        for rank in self.text_ranks:
            self.screen.blit(rank[0], rank[1])

    def events(self, event=None):
        """
        Press any key to exchange the panel
        :return:
        """
        if event and (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP):
            self.GUI_settings.game_stage = 0
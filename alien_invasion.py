import sys

import pygame
import ship


class MainGame:
    def __init__(self, settings):
        self.settings = settings

        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption(settings.game_title)
        self.ship = ship.Ship(self.screen)

    def start(self):
        '''Run the game'''
        while True:
            # Watch for keyboard and mouse events.
            self.check_events()
            self.ship.move()
            # Update the images on the screen and flip the new screen
            self.update_screen()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if click the right-top 'x' button, quit the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # KEYDOWN cannot do smoothly continuous response
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.move_state = 'R'
                elif event.key == pygame.K_LEFT:
                    self.ship.move_state = 'L'
                elif event.key == pygame.K_UP:
                    self.ship.move_state = 'U'
                elif event.key == pygame.K_DOWN:
                    self.ship.move_state = 'D'
                else:
                    self.ship.move_state = ''
            elif event.type == pygame.KEYUP:  # KEYDOWN and KEYUP pair makes the motion smoothly and continuously
                self.ship.move_state = ''

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()  # draw the ship
        # Make the most recently drawn screen visible.
        pygame.display.flip()
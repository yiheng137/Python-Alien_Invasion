import sys

import pygame
import ship
import settings
import alien
from pygame.sprite import Group
from game_functions import *


class MainGame:
    def __init__(self, penal_settings):
        self.penal_settings = penal_settings

        pygame.init()
        self.screen = pygame.display.set_mode((penal_settings.screen_width, penal_settings.screen_height))
        pygame.display.set_caption(penal_settings.game_title)

        # create the ship object with its settings
        self.ai_settings = settings.AISettings()
        self.ship = ship.Ship(self.ai_settings, self.screen)

        # Make a group to store aliens
        self.alien_lst = Group()
        create_fleet(self.ai_settings, self.screen, self.alien_lst)

        # Make a group to store bullets.
        self.bullet_lst = Group()

    def start(self):
        '''Run the game'''
        while True:
            # Watch for keyboard and mouse events.
            self.__check_events()
            self.__update_objects()
            # Update the images on the screen and flip the new screen
            self.__update_screen()

    def __check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if click the right-top 'x' button, quit the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # KEYDOWN cannot do smoothly continuous response
                self.__keydown_events(event)
            elif event.type == pygame.KEYUP:  # KEYDOWN and KEYUP pair makes the motion smoothly and continuously
                self.__keyup_events(event)

    def __keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            fire_bullet(self.ai_settings, self.screen, self.ship, self.bullet_lst)
        elif event.key == pygame.K_RIGHT:
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

    def __keyup_events(self, event):
        self.ship.move_state = ''

    def __update_objects(self):
        """update the position of all objects"""
        self.ship.move() # update the ship positions

        # update the bullets positions
        self.bullet_lst.update()
        # Get rid of bullets that has disappeared.
        for bullet in self.bullet_lst.copy():
            if bullet.y <= 0:
                self.bullet_lst.remove(bullet)

    def __update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.penal_settings.bg_color)
        self.ship.blit()  # draw the ship

        # Draw the aliens
        self.alien_lst.draw(self.screen)

        # Redraw all bullets behind ship and aliens.
        for bullet in self.bullet_lst.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
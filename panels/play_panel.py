from time import sleep

import pygame
import alien_fleet
import bullet
import ship
from pygame.sprite import Group


class PlayPanel:
    """
    Implement the GUI of the game play panel
    """

    def __init__(self, settings, screen, game_states):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.ai_settings = settings.ai_settings
        self.GUI_settings = settings.GUI_settings
        self.panel_settings = settings.panel_settings
        self.game_states = game_states

        # create the ship object with its settings
        self.ship = ship.Ship(self.ai_settings, self.screen)

        # Make a group to store aliens
        self.alien_fleet = alien_fleet.AlienFleet(self.ai_settings, self.screen)

        # Make a group to store bullets.
        self.bullet_lst = Group()

    def show(self):
        """
        Show the GUI of the play panel
        :return:
        """
        self.__update_objects()
        # Update the images on the screen and flip the new screen
        self.__update_screen()
        # Check whether the game is over
        self.__check_game_over()

    def events(self, event=None):
        """Respond to keypresses and mouse events."""
        if event:
            if event.type == pygame.KEYDOWN:  # KEYDOWN cannot do smoothly continuous response
                self.__keydown_events(event)
            elif event.type == pygame.KEYUP:  # KEYDOWN and KEYUP pair makes the motion smoothly and continuously
                self.__keyup_events(event)

    def __keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_SPACE:
            # Create a new bullet and add it to the bullets group.
            self.fire_bullet(self.ai_settings, self.screen, self.ship, self.bullet_lst)

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.move_state = 'E'
        elif event.key == pygame.K_LEFT:
            self.ship.move_state = 'W'
        elif event.key == pygame.K_UP:
            self.ship.move_state = 'N'
        elif event.key == pygame.K_DOWN:
            self.ship.move_state = 'S'

    def __keyup_events(self, event):
        if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
            self.ship.move_state = ''

    def __update_objects(self):
        """update the position of all objects"""
        self.__update_ship()
        self.__update_bullets()
        self.__update_aliens()

    def __update_ship(self):
        self.ship.move()  # update the ship positions

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.alien_fleet.alien_list):
            self.__ship_hit()

    def __ship_hit(self):
        """Respond to ship being hit by alien."""
        # Decrement ships_left.
        self.game_states.ships_left -= 1
        self.ship.center_ship()
        sleep(0.5)

    def __aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        return self.alien_fleet.check_fleet_bottom()

    def __check_game_over(self):
        if self.game_states.ships_left <= 0 or self.__aliens_bottom():
            self.game_states.update_rank()
            self.game_states.reset_stats()
            self.GUI_settings.game_stage = 2

    def __update_bullets(self):
        # update the bullets positions
        self.bullet_lst.update()

        # Get rid of bullets that has disappeared.
        for bullet in self.bullet_lst.copy():
            if bullet.pos[1] <= 0:
                self.bullet_lst.remove(bullet)

        self.__check_bullet_alien_collisions()

    def __update_aliens(self):
        self.alien_fleet.update_fleet()

    def __check_bullet_alien_collisions(self):
        """Check for any bullets that have hit aliens.
           If so, get rid of the bullt and the alien."""

        collisions = pygame.sprite.groupcollide(self.bullet_lst, self.alien_fleet.alien_list, True, True)
        self.game_states.score += len(collisions) * 50  # compute the score
        if self.alien_fleet.empty():
            # Destory existing bullets and create new fleet.
            self.bullet_lst.empty()
            self.alien_fleet = alien_fleet.AlienFleet(self.ai_settings, self.screen)

    def __update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.panel_settings.bg_color)
        self.ship.draw()  # draw the ship

        # Draw the aliens
        self.alien_fleet.draw_fleet()

        # Redraw all bullets behind ship and aliens.
        for bullet in self.bullet_lst.sprites():
            bullet.draw()

        # Draw the player's hearts
        self.game_states.display()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def fire_bullet(self, ai_settings, screen, ship, bullet_lst):
        """Create a new bullet and add it to the bullets group."""
        # Limit the number of bullet on the screen
        if len(bullet_lst) < ai_settings.bullet_allowed:
            new_bullet = bullet.Bullet(ai_settings, screen, ship)
            bullet_lst.add(new_bullet)
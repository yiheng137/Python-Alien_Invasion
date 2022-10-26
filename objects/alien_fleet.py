import pygame.sprite as sprite
import alien


class AlienFleet:
    """This class controls the alien fleet methods and attributes"""

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.move_speed = ai_settings.fleet_speed  # indicate the current speed of the fleet
        self.alien_list = sprite.Group()
        self.fleet_direction = 1  # control the movement direction of the entire fleet
        self.create_fleet()  # create the fleet according to the provided information

    def __get_number_aliens_cols(self):
        """Determine the number of aliens that fit in a row."""
        available_space_x = self.screen_width - 2 * self.ai_settings.alien_size[0]
        return int(available_space_x / (2 * self.ai_settings.alien_size[0]))

    def __get_number_aliens_rows(self):
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = self.screen_height - 3 * self.ai_settings.alien_size[1] - self.ai_settings.ship_size[1]
        return int(available_space_y / (2 * self.ai_settings.alien_size[1]))

    def __create_alien(self, col_index, row_index):
        """Create an alien and place it in the row"""
        new_alien = alien.Alien(self.ai_settings, self.screen)
        new_alien.pos[0] = (2 * col_index + 1) * new_alien.rect.width
        new_alien.pos[1] = (2 * row_index + 1) * new_alien.rect.height
        new_alien.rect.x = int(new_alien.pos[0])
        new_alien.rect.y = int(new_alien.pos[1])
        new_alien.move_speed = [self.move_speed[0], 0]  # reset the alien speed
        self.alien_list.add(new_alien)

    def create_fleet(self):
        """Create a full fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        number_col = self.__get_number_aliens_cols()
        number_row = self.__get_number_aliens_rows()

        # Create the first row of aliens.
        for row_index in range(number_row):
            for col_index in range(number_col):
                # Create an alien and place it in the row.
                self.__create_alien(col_index, row_index)

    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.alien_list.sprites():
            alien.rect.y += self.move_speed[1]  # move down
            alien.move_speed[0] *= -1

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.alien_list.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def check_fleet_bottom(self):
        """Check if any aliens have reached to bottom of the screen."""
        for alien in self.alien_list.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                return True
        return False

    def update_fleet(self):
        """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        self.alien_list.update()

    def draw_fleet(self):
        """Draw the alian fleet on the screen"""
        self.alien_list.draw(self.screen)

    def empty(self):
        """Check if the fleet is empty of not"""
        if len(self.alien_list):
            return False
        return True
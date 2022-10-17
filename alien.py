import pygame
import CClass
import utils
from pygame.sprite import Sprite


class Alien(Sprite, CClass.CObject):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        Sprite.__init__(self)
        CClass.CObject.__init__(self, ai_settings, screen, pygame.image.load(ai_settings.alien_img_path))

        # Load the alien image and set its rect attribute.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width // 2
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.pos = [float(self.rect.x), self.rect.height / 2]
        self.move_range = utils.get_move_range(self.rect, self.screen_rect)

        # Store the alien information from settings
        self.move_speed = [ai_settings.alien_speed[0], 0]

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def draw(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right."""
        self.pos[0] += self.move_speed[0]
        self.rect.x = round(self.pos[0])

        # self.pos[1] += self.move_speed[1]
        # self.rect.y = round(self.pos[1])



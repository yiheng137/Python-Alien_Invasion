import pygame
import CClass
from pygame.sprite import Sprite  # group related elements and act on all the grouped elements at once


class Bullet(Sprite, CClass.CObject):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        Sprite.__init__(self)
        CClass.CObject.__init__(self, ai_settings=ai_settings, screen=screen)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_size[0], ai_settings.bullet_size[1])
        self.rect.centerx = ship.rect.centerx  # bind the x position of bullet to ship position
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.pos = [0, float(self.rect.y)]

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        """Move the bullet up the screen. Note that this method overwrites the same method in pygame.sprite.Group"""
        # Update the decimal position of the bullet. The bullits can only move vertically
        self.pos[1] -= self.speed
        # Update the rect position.
        self.rect.y = round(self.pos[1])

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

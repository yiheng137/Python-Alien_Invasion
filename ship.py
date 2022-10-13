import pygame

class Ship:

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Specified properties of the ship
        self.move_speed = 1  # how fast the ship will move
        self.move_state = ''  # decide which orientation the ship will move
        self.move_range = (self.rect.width // 2,  # minimum x
                           self.screen_rect.width - self.rect.width // 2,  # maximum x
                           self.rect.height // 2,  # minimum y,
                           self.screen_rect.height - self.rect.height // 2)  # restrict the motion position of the ship on the screen

    def move(self):
        """Change the position of the ship according to self.move_state"""
        if self.move_state == 'R':
            # consider the motion boundary
            self.rect.centerx = min(self.rect.centerx + self.move_speed, self.move_range[1])
        elif self.move_state == 'L':
            self.rect.centerx = max(self.rect.centerx - self.move_speed, self.move_range[0])
        elif self.move_state == 'U':
            self.rect.centery = max(self.rect.centery - self.move_speed, self.move_range[2])
        elif self.move_state == 'D':
            self.rect.centery = min(self.rect.centery + self.move_speed, self.move_range[3])

    def blit(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
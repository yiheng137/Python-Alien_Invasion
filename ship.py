import pygame

class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # the rect of the ship
        self.screen_rect = screen.get_rect()

        # Specified properties of the ship
        self.move_speed = self.ai_settings.ship_speed  # how fast the ship will move
        self.move_state = ''  # decide which orientation the ship will move
        self.move_range = (self.rect.width // 2,  # minimum x
                           self.screen_rect.width - self.rect.width // 2,  # maximum x
                           self.rect.height // 2,  # minimum y,
                           self.screen_rect.height - self.rect.height // 2)  # restrict the motion position of the ship on the screen

        # specify the position of the ship
        # note the self.rect.centerx/centery only stores int value. Need to use pos to store float values for the movement
        if self.ai_settings.ship_pos:
            self.pos = self.ai_settings.ship_pos
        else:
            self.pos = [float(self.screen_rect.centerx), float(self.screen_rect.height - self.rect.height / 2)]

        # Start each new ship at the bottom center of the screen.
        self._update_rect(True)

    def _verify_pos(self):
        """Verify the positions. If it is out of the boundary, correct it"""
        # check x coordinate
        if self.pos[0] > self.move_range[1]:
            self.pos[0] = self.move_range[1]
        elif self.pos[0] < self.move_range[0]:
            self.pos[0] = self.move_range[0]

        # check y coordinate
        if self.pos[1] > self.move_range[3]:
            self.pos[1] = self.move_range[3]
        elif self.pos[1] < self.move_range[2]:
            self.pos[1] = self.move_range[2]

    def _update_rect(self, out_of_bound=False):
        """update the ship rect according to its position. If verift is True, correct the position that cannot exceed
        the boundary"""
        if not out_of_bound:
            self._verify_pos()
        self.rect.centerx = round(self.pos[0])
        self.rect.centery = round(self.pos[1])

    def move(self, out_of_bound=False):
        """Change the position of the ship according to self.move_state.
        out_of_bound: decide whether the ship can go out of the boundary"""
        if self.move_state == 'R':
            # consider the motion boundary
            self.pos[0] += self.move_speed
        elif self.move_state == 'L':
            self.pos[0] -= self.move_speed
        elif self.move_state == 'U':
            self.pos[1] -= self.move_speed
        elif self.move_state == 'D':
            self.pos[1] += self.move_speed

        # update the rect of ship
        self._update_rect(out_of_bound=out_of_bound)

    def blit(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
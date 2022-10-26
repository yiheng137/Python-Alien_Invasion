import CClass


class Ship(CClass.CObject):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__(ai_settings, screen, ai_settings.ship_img_path, ai_settings.ship_size)
        """Initialize the ship and set its starting position."""

        # Get the ship's rect.
        self.rect = self.image.get_rect()  # the rect of the ship
        self.screen_rect = screen.get_rect()

        # Specified properties of the ship
        self.move_speed = self.settings.ship_speed  # how fast the ship will move
        self.move_state = ''  # decide which orientation the ship will move
        self.move_range = self._get_move_range(self.rect, self.screen_rect)

        # specify the position of the ship
        # note the self.rect.centerx/centery only stores int value. Need to use pos to store float values for the movement
        if self.settings.ship_init_pos:
            self.pos = self.settings.ship_pos
        else:
            self.pos = [float(self.screen_rect.centerx), float(self.screen_rect.height - self.rect.height / 2)]

        # Start each new ship at the bottom center of the screen.
        self._update_rect(True)

    def _update_rect(self, out_of_bound=False):
        """update the ship rect according to its position. If verift is True, correct the position that cannot exceed
        the boundary"""

        if not out_of_bound:
            self._verify_pos()
        self.rect.centerx = round(self.pos[0])
        self.rect.centery = round(self.pos[1])

    def move(self, out_of_bound=False):
        """Change the position of the ship according to self.move_state.
        out_of_bound: decide whether the ship can go out of the boundary.
        Override the same method in CClass.CObject.move()"""

        if self.move_state == 'E':
            # consider the motion boundary
            self.pos[0] += self.move_speed
        elif self.move_state == 'W':
            self.pos[0] -= self.move_speed
        elif self.move_state == 'N':
            self.pos[1] -= self.move_speed
        elif self.move_state == 'S':
            self.pos[1] += self.move_speed

        # update the rect of ship
        self._update_rect(out_of_bound=out_of_bound)

    def center_ship(self):
        """Center the ship on the screen."""
        if self.settings.ship_init_pos:
            self.pos = self.settings.ship_pos
        else:
            self.pos = [float(self.screen_rect.centerx), float(self.screen_rect.height - self.rect.height / 2)]
        self.rect.centerx = round(self.pos[0])
        self.rect.centery = round(self.pos[1])
        self.move_state = ''

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
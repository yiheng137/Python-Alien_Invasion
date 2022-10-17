"""This code is to store all customized classes"""

class CObject:
    """This class is the basic object class that has the basic methods and variables"""

    def __init__(self, ai_settings, screen, image=None):
        self.screen = screen  # main screen where the object will appear
        self.rect = None
        self.settings = ai_settings
        self.image = image
        self.pos = None  # the virtual position of the object (float)
        self.move_range = None
        self.move_speed = [0.0, 0.0]
        self.move_state = ''  # decide the orientation of the motion from 'w', 's', 'n', 'e', and '' for no movement

    def draw(self):
        """Draw the object on the screen"""
        pass

    def move(self):
        """Update the virtual position"""
        pass

    def _verify_pos(self):
        """Verify the positions. If it is out of the boundary, correct it.
        Return true if the position is verified."""

        if self.pos and self.move_range:
            flag = ''
            # check x coordinate
            if self.pos[0] > self.move_range[1]:
                self.pos[0] = self.move_range[1]
                flag = 'E'
            elif self.pos[0] < self.move_range[0]:
                self.pos[0] = self.move_range[0]
                flag = 'W'

            # check y coordinate
            if self.pos[1] > self.move_range[3]:
                self.pos[1] = self.move_range[3]
                flag = 'S'
            elif self.pos[1] < self.move_range[2]:
                self.pos[1] = self.move_range[2]
                flag = 'N'
            return flag

    def _check_edges(self):
        """Return the direction of the object if it hit the boundary"""
        if self.rect and self.screen:
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                self.pos[0] = screen_rect.right
                return 'E'
            elif self.rect.left <= 0:
                self.pos[0] = 0
                return 'W'
            elif self.rect.top <= 0:
                self.pos[1] = 0
                return 'N'
            elif self.rect.bottom >= screen_rect.bottom:
                self.pos[1] = screen_rect.bottom
                return 'S'
            else:
                return ''

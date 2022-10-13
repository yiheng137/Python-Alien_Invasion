"""This code is to store all customized classes"""

class CObject:
    """This class is the basic object class that has the basic methods and variables"""

    def __init__(self, settings, screen):
        self.screen = screen  # main screen where the object will appear
        self.pos = None  # the virtual position of the object (float)
        self.rect = None  # the information of the actual rect box of the object
        self.speed = 1.0  # the speed of the movement
        self.move_state = ''  # decide the orientation of the motion from 'w', 's', 'n', 'e', and '' for no movement

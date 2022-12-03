from constants import *
from game.scripting.action import Action


class ControlPacmanAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            pacman.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            pacman.swing_right()
        elif self._keyboard_service.is_key_down(UP): 
            pacman.swing_up() 
        elif self._keyboard_service.is_key_down(DOWN): 
            pacman.swing_down()  
        # else: 
        #     pacman.stop_moving()
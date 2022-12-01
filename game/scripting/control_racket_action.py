from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        if self._keyboard_service.is_key_down(UP):
            pacman.move_up()
        elif self._keyboard_service.is_key_down(RIGHT): 
            pacman.move_right()  
        elif self._keyboard_service.is_key_down(DOWN):
            pacman.move_down()
        elif self._keyboard_service.is_key_down(LEFT): 
            pacman.move_left()
        else: 
            pacman.stop_moving()        
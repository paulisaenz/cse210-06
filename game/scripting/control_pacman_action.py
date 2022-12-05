from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class ControlPacmanAction(Action):

    def __init__(self, keyboard_service, physics_service):
        self._keyboard_service = keyboard_service
        self._physics_service = physics_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()
        direction = pacman.get_direction()
        paths = cast.get_actors(PATH_GROUP)

        for path in paths:

            path_body = path.get_body()
            directions = path.get_directions()


            if self._physics_service.has_collided(pacman_body, path_body):
                pacman_body.set_velocity(Point(0, 0))
                if "u" in directions:
                    if self._keyboard_service.is_key_down(UP): 
                        pacman.swing_up() 
                if "r" in directions:
                    if self._keyboard_service.is_key_down(RIGHT): 
                        pacman.swing_right()
                if "d" in directions:
                    if self._keyboard_service.is_key_down(DOWN): 
                        pacman.swing_down() 
                if "l" in directions:
                    if self._keyboard_service.is_key_down(LEFT):
                        pacman.swing_left()
        
        if direction == "up":
            if self._keyboard_service.is_key_down(DOWN): 
                pacman.swing_down()
        elif direction == "right":
            if self._keyboard_service.is_key_down(LEFT):
                pacman.swing_left()
        elif direction == "down":
            if self._keyboard_service.is_key_down(UP): 
                pacman.swing_up()
        elif direction == "left":
            if self._keyboard_service.is_key_down(RIGHT):
                pacman.swing_right()
            
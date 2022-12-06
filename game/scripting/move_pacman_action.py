from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MovePacmanAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        body = pacman.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)
        y = position.get_y()

        if x < 0:
            position = Point(SCREEN_WIDTH - PACMAN_WIDTH, y)
        elif x > (SCREEN_WIDTH - PACMAN_WIDTH):
            position = Point(0, y)
            
        body.set_position(position)
        
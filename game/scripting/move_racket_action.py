from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        body = pacman.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(SCREEN_WIDTH - PACMAN_WIDTH, position.get_y())
        elif x > (SCREEN_WIDTH - PACMAN_WIDTH):
            position = Point(0, position.get_y())

        if y < FIELD_TOP:
            position = Point(position.get_x(), SCREEN_HEIGHT - PACMAN_HEIGHT)
        elif y > (SCREEN_HEIGHT - PACMAN_HEIGHT):
            position = Point(position.get_x(), FIELD_TOP)
            
        body.set_position(position)
        
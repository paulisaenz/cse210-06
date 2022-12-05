from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveGhostAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        for ghost in cast.get_actors(GHOST_GROUP):
            body = ghost.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            x = position.get_x()

            position = position.add(velocity)
            
            if x < 0:
                position = Point(SCREEN_WIDTH - GHOST_WIDTH, position.get_y())
            elif x > (SCREEN_WIDTH - GHOST_WIDTH):
                position = Point(0, position.get_y())
                
            body.set_position(position)

from constants import *
from random import randint
from game.casting.point import Point
from game.scripting.action import Action


class ControlGhostAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service
        
    def execute(self, cast, script, callback):
        ghosts = cast.get_actors(GHOST_GROUP)
        for ghost in ghosts:

            ghost_body = ghost.get_body()
            direction = ghost.get_direction()
            paths = cast.get_actors(PATH_GROUP)

            if ghost_body.get_position().get_x() == 210 and ghost_body.get_position().get_y() == 229 + FIELD_TOP:
                self._turn_ghost(ghost, "u")
                ghost.set_direction("s")
            if ghost_body.get_position().get_x() == 178 and ghost_body.get_position().get_y() == 229 + FIELD_TOP:
                self._turn_ghost(ghost, "r")
                ghost.set_direction("s")
            if ghost_body.get_position().get_x() == 242 and ghost_body.get_position().get_y() == 229 + FIELD_TOP:
                self._turn_ghost(ghost, "l")
                ghost.set_direction("s")
            if ghost_body.get_position().get_x() == 210 and ghost_body.get_position().get_y() <= 170 + FIELD_TOP and ghost.get_direction() == "s":
                directions = ["r", "l"]
                direction = directions[randint(0, len(directions)-1)]
                self._turn_ghost(ghost, direction)

            for path in paths:

                path_body = path.get_body()
                directions = path.get_directions()

                if self._physics_service.has_collided(ghost_body, path_body):
                    if direction not in directions:
                        ghost_body.set_velocity(Point(0, 0))

                    
                    direction = directions[randint(0, len(directions)-1)]

                    self._turn_ghost(ghost, direction)
                    
    def _turn_ghost(self, ghost, direction):
        if direction == "u":
            ghost.swing_up()
        elif direction == "r":
            ghost.swing_right()
        elif direction == "d":
            ghost.swing_down()
        elif direction == "l":
            ghost.swing_left()
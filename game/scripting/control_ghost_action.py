from constants import *
from random import randint
from game.casting.point import Point
from game.scripting.action import Action
from game.casting.animation import Animation


class ControlGhostAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service
        
    def execute(self, cast, script, callback):
        ghosts = cast.get_actors(GHOST_GROUP)

        blinky_ani = []
        blinky_ani.append(Animation(BLINKY_IMAGES["up"], GHOST_RATE))
        blinky_ani.append(Animation(BLINKY_IMAGES["right"], GHOST_RATE))
        blinky_ani.append(Animation(BLINKY_IMAGES["down"], GHOST_RATE))
        blinky_ani.append(Animation(BLINKY_IMAGES["left"], GHOST_RATE))
        pinky_ani = []
        pinky_ani.append(Animation(PINKY_IMAGES["up"], GHOST_RATE))
        pinky_ani.append(Animation(PINKY_IMAGES["right"], GHOST_RATE))
        pinky_ani.append(Animation(PINKY_IMAGES["down"], GHOST_RATE))
        pinky_ani.append(Animation(PINKY_IMAGES["left"], GHOST_RATE))
        inky_ani = []
        inky_ani.append(Animation(INKY_IMAGES["up"], GHOST_RATE))
        inky_ani.append(Animation(INKY_IMAGES["right"], GHOST_RATE))
        inky_ani.append(Animation(INKY_IMAGES["down"], GHOST_RATE))
        inky_ani.append(Animation(INKY_IMAGES["left"], GHOST_RATE))
        clyed_ani = []
        clyed_ani.append(Animation(CLYDE_IMAGES["up"], GHOST_RATE))
        clyed_ani.append(Animation(CLYDE_IMAGES["right"], GHOST_RATE))
        clyed_ani.append(Animation(CLYDE_IMAGES["down"], GHOST_RATE))
        clyed_ani.append(Animation(CLYDE_IMAGES["left"], GHOST_RATE))
        eye_ani = []
        eye_ani.append(Animation(EYE_IMAGES["up"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["right"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["down"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["left"], GHOST_RATE))
        
        for ghost in ghosts:

            ghost_body = ghost.get_body()
            direction = ghost.get_direction()
            paths = cast.get_actors(PATH_GROUP)
            target = None

            if ghost_body.get_position().get_x() == 210 and ghost_body.get_position().get_y() == 229 + FIELD_TOP:
                self._turn_ghost(ghost, "u")
                ghost.set_direction("s")
                ghost.set_state("g")


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
            
            if ghost_body.get_position().get_x() == 210 and ghost_body.get_position().get_y() <= 170 + FIELD_TOP and ghost.get_state() == "e":

                name = ghost.get_name()
                if name == "Blinky":
                    ghost.set_animation(blinky_ani)
                elif name == "Pinky":
                    ghost.set_animation(pinky_ani)
                elif name == "Inky":
                    ghost.set_animation(inky_ani)
                elif name == "Clyde":
                    ghost.set_animation(clyed_ani)
                else:
                    ghost.set_animation(eye_ani)

            if ghost.get_state() == "e":
                target = Point(210, 229 + FIELD_TOP)

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
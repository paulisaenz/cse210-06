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
        
        for ghost in ghosts:
            
            ghost_body = ghost.get_body()
            ghost_x, ghost_y = ghost_body.get_position().get_x(), ghost_body.get_position().get_y()
            direction = ghost.get_direction()
            paths = cast.get_actors(PATH_GROUP)
            target = None
            
            if ghost.get_state() != "wait":
                if ghost_x == 178 and ghost_y == 229 + FIELD_TOP:
                    self._turn_ghost(ghost, "r")
                    ghost.set_state("start")

                if ghost_x == 242 and ghost_y == 229 + FIELD_TOP:
                    self._turn_ghost(ghost, "l")
                    ghost.set_state("start")
                            
                if ghost.get_state() == "dead":
                    target = Point(210, 170 + FIELD_TOP)
                    travel_x = ghost_x - target.get_x()
                    travel_y = ghost_y - target.get_y()

                for path in paths:

                    path_body = path.get_body()
                    directions = path.get_directions()

                    if self._physics_service.has_collided(ghost_body, path_body):
                        prev_direction = direction

                        if path.get_number() == 90 and ghost.get_state() == "dead":
                            self._turn_ghost(ghost, "d")
                        elif path.get_number() == 91:
                            self._turn_ghost(ghost, "r")
                            ghost.set_state("start")
                        elif path.get_number() == 93:
                            self._turn_ghost(ghost, "l")
                            ghost.set_state("start")

                        elif path.get_number() == 92 and (ghost.get_state() in ["start", "dead"]):
                            if ghost.get_name() == "Blinky":
                                ghost.set_animation(blinky_ani)
                            elif ghost.get_name() == "Pinky":
                                ghost.set_animation(pinky_ani)
                            elif ghost.get_name() == "Inky":
                                ghost.set_animation(inky_ani)
                            elif ghost.get_name() == "Clyde":
                                ghost.set_animation(clyed_ani)

                            self._turn_ghost(ghost, "u")
                            ghost.set_state("ghost")
                        
                        elif path.get_number() == 90 and ghost.get_state() == "start":
                            ghost.set_state("ghost")
                        else:
                            if ghost.get_state() == "dead":
                                if path.get_number() in [37, 49, 56]:
                                    direction = "r"
                                elif path.get_number() in [36, 42, 55]:
                                    direction = "l"
                                else:
                                    direction = self._return_home(travel_x, travel_y, prev_direction, directions)
                                
                            else:
                                direction = directions[randint(0, len(directions)-1)]
                                while self._is_opposite(prev_direction, direction):
                                    direction = directions[randint(0, len(directions)-1)]
                            self._turn_ghost(ghost, direction)
                            
                            if direction not in directions:
                                ghost_body.set_velocity(Point(0, 0))
                        
                    
    def _turn_ghost(self, ghost, direction):
        if direction == "u":
            ghost.swing_up()
        elif direction == "r":
            ghost.swing_right()
        elif direction == "d":
            ghost.swing_down()
        elif direction == "l":
            ghost.swing_left()
        
    def _is_opposite(self, prev_direction, direction):
        if prev_direction == "u" and direction == "d":
            return True
        elif prev_direction == "d" and direction == "u":
            return True
        elif prev_direction == "r" and direction == "l":
            return True
        elif prev_direction == "l" and direction == "r":
            return True
        else:
            return False
        
    def _return_home(self, travel_x, travel_y, prev_direction, directions):
        if prev_direction == "u":
            if travel_y > 0 and "u" in directions:
                direction = "u"
            elif travel_x < 0 and "r" in directions:
                direction = "r"
            elif travel_x > 0 and "l" in directions:
                direction = "l"
            else:
                direction = directions[randint(0, len(directions)-1)]

        elif prev_direction == "d":
            if travel_y < 0 and "d" in directions:
                direction = "d"
            elif travel_x < 0 and "r" in directions:
                direction = "r"
            elif travel_x > 0 and "l" in directions:
                direction = "l"
            else:
                direction = directions[randint(0, len(directions)-1)]

        elif prev_direction == "r":
            if travel_y > 0 and "u" in directions:
                direction = "u"
            elif travel_y < 0 and "d" in directions:
                direction = "d"
            elif travel_x < 0 and "r" in directions:
                direction = "r"
            else:
                direction = directions[randint(0, len(directions)-1)]

        elif prev_direction == "l":
            if travel_y > 0 and "u" in directions:
                direction = "u"
            elif travel_y < 0 and "d" in directions:
                direction = "d"
            elif travel_x > 0 and "l" in directions:
                direction = "l"
            else:
                direction = directions[randint(0, len(directions)-1)]
        else:
            direction = directions[randint(0, len(directions)-1)]
        
        return direction
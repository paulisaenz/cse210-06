from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.animation import Animation


class CollidePelletsAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()

        pellets = cast.get_actors(PELLET_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        chomp_sound = Sound(CHOMP_SOUND)
        power_pellet_sound = Sound(POWER_PELLET_SOUND)

        ghosts = cast.get_actors(GHOST_GROUP)
        scared_ani = []
        scared_ani.append(Animation(SCARED_IMAGES["up"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["right"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["down"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["left"], GHOST_RATE))
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
            # scared ghost countdown will be 10 seconds
            if ghost.get_state() == "scared":
                self._scared_ghost_countdown = self._scared_ghost_countdown - 1
                print(self._scared_ghost_countdown)
                if self._scared_ghost_countdown < 1:
                    ghost.set_state("ghost")
                    if ghost.get_name() == "Blinky":
                        ghost.set_animation(blinky_ani)
                    elif ghost.get_name() == "Pinky":
                        ghost.set_animation(pinky_ani)
                    elif ghost.get_name() == "Inky":
                        ghost.set_animation(inky_ani)
                    elif ghost.get_name() == "Clyde":
                        ghost.set_animation(clyed_ani)

        for pellet in pellets:

            path_body = pellet.get_body()

            if self._physics_service.has_collided(pacman_body, path_body):

                if pellet.get_points() == POWER_PELLET_POINTS:
                    self._audio_service.play_sound(power_pellet_sound)
                    stats.add_points(POWER_PELLET_POINTS)

                    for ghost in ghosts:
                        if ghost.get_state() != "dead":
                            ghost.set_animation(scared_ani)
                            ghost.set_state("scared")
                else:
                    self._audio_service.play_sound(chomp_sound)
                    stats.add_points(PELLET_POINTS)

                cast.remove_actor(PELLET_GROUP, pellet)

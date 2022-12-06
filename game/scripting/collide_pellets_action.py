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

        ghosts = cast.get_actors(GHOST_GROUP)
        scared_ani = []
        scared_ani.append(Animation(SCARED_IMAGES["up"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["right"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["down"], GHOST_RATE))
        scared_ani.append(Animation(SCARED_IMAGES["left"], GHOST_RATE))
        
        for pellet in pellets:

            path_body = pellet.get_body()

            if self._physics_service.has_collided(pacman_body, path_body):
                self._audio_service.play_sound(chomp_sound)
                stats.add_points(PELLET_POINTS)
                cast.remove_actor(PELLET_GROUP, pellet)

                if pellet.get_points() == POWER_PELLET_POINTS:
                    for ghost in ghosts:
                        ghost.set_animation(scared_ani)
                
                    


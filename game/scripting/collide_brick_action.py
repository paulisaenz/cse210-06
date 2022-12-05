from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()
        pacman_pos = pacman_body.get_position()
        pmx, pmy = pacman_pos.get_x(), pacman_pos.get_y()

        ghosts = cast.get_actors(GHOST_GROUP)
        paths = cast.get_actors(PATH_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for path in paths:

            path_body = path.get_body()
            path_pos = path_body.get_position()
            px, py = path_pos.get_x(), path_pos.get_y()


            if self._physics_service.has_collided(pacman_body, path_body):
                pacman_body.set_velocity(Point(0, 0))
                
                    


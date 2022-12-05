from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollidePelletsAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()

        pellets = cast.get_actors(PELLET_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for pellet in pellets:

            path_body = pellet.get_body()

            if self._physics_service.has_collided(pacman_body, path_body):
                cast.remove_actor(PELLET_GROUP, pellet)
                
                    


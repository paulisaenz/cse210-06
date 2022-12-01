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
        ghosts = cast.get_actors(GHOST_GROUP)
        walls = cast.get_actors(WALL_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for wall in walls:
            pacman_body = pacman.get_body()
            pacman_pos = pacman_body.get_position()

            wall_body = wall.get_body()

            if self._physics_service.has_collided(pacman_body, wall_body):
                sound = Sound(BOUNCE_SOUND)
                # self._audio_service.play_sound(sound)

                px, py = pacman_pos.get_x(), pacman_pos.get_y()

                if self._physics_service.is_left_of(pacman_body, wall_body):
                    pacman_body.set_position(Point(px - WALL_THRESHOLD, py))

                elif self._physics_service.is_right_of(pacman_body, wall_body):
                    pacman_body.set_position(Point(px + WALL_THRESHOLD, py))
                
                if self._physics_service.is_below(pacman_body, wall_body):
                    pacman_body.set_position(Point(px, py + WALL_THRESHOLD))
                
                elif self._physics_service.is_above(pacman_body, wall_body):
                    pacman_body.set_position(Point(px, py - WALL_THRESHOLD))


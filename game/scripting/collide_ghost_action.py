from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.animation import Animation


class CollideGhostAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ghosts = cast.get_actors(GHOST_GROUP)
        pacman = cast.get_first_actor(PACMAN_GROUP)
        pacman_body = pacman.get_body()

        stats = cast.get_first_actor(STATS_GROUP)

        eye_ani = []
        eye_ani.append(Animation(EYE_IMAGES["up"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["right"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["down"], GHOST_RATE))
        eye_ani.append(Animation(EYE_IMAGES["left"], GHOST_RATE))

        for ghost in ghosts:
            
            ghost_body = ghost.get_body()
            if self._physics_service.has_collided(ghost_body, pacman_body):
                if ghost.get_state() == "scared":
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    stats.add_points(GHOST_POINTS)
                    ghost.set_state("dead")
                    ghost.set_animation(eye_ani)
                elif ghost.get_state() == "ghost":
                    stats.lose_life()

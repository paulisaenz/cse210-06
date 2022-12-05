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

        animations = []
        animations.append(Animation(EYE_IMAGES["up"], GHOST_RATE))
        animations.append(Animation(EYE_IMAGES["right"], GHOST_RATE))
        animations.append(Animation(EYE_IMAGES["down"], GHOST_RATE))
        animations.append(Animation(EYE_IMAGES["left"], GHOST_RATE))

        for ghost in ghosts:
            
            ghost_body = ghost.get_body()
            if self._physics_service.has_collided(ghost_body, pacman_body):
                if ghost.get_state() == "g":
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)

                ghost.set_state("e")
                ghost.set_animation(animations)
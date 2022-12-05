from constants import *
from game.scripting.action import Action


class DrawPacmanAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        pacman = cast.get_first_actor(PACMAN_GROUP)
        body = pacman.get_body()

        if pacman.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = pacman.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
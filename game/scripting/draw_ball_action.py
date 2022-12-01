from constants import *
from game.scripting.action import Action


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        for ghost in cast.get_actors(GHOST_GROUP):
            body = ghost.get_body()

            if ghost.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
            
            animation = ghost.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
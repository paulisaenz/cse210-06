from constants import *
from game.scripting.action import Action


class DrawPelletsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        pellets = cast.get_actors(PELLET_GROUP)
        
        for pellet in pellets:
            body = pellet.get_body()

            if pellet.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = pellet.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
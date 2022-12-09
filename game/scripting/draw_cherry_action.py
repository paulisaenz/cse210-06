from constants import *
from game.scripting.action import Action


class DrawCherryAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        cherries = cast.get_actors(CHERRY_GROUP)
        
        for cherry in cherries:
            body = cherry.get_body()

            if cherry.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = cherry.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
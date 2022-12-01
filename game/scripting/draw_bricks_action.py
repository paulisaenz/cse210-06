from constants import *
from game.scripting.action import Action


class DrawBricksAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(WALL_GROUP)
        
        for brick in bricks:
            body = brick.get_body()

            if brick.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = brick.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

        bg = cast.get_first_actor(BG_GROUP)
        body = bg.get_body()

        if bg.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = bg.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
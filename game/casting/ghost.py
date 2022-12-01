import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ghost(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Ghost.

        Args:
            body: A new instance of Body.
            animation: A new instance of animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animations = animation
        self._animation = self._animations[0]
    
    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def move_up(self):
        """Moves the Ghost up."""
        velocity = Point(0, -GHOST_VELOCITY)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_UP]

    def move_right(self):
        """Moves PacMan right."""
        velocity = Point(GHOST_VELOCITY, 0)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_RIGHT]

    def move_down(self):
        """Moves PacMan down."""
        velocity = Point(0, GHOST_VELOCITY)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_DOWN]
        
    def move_left(self):
        """Moves PacMan left."""
        velocity = Point(-GHOST_VELOCITY, 0)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_LEFT]

    def get_body(self):
        """Gets the Ghost's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the Ghost's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self, direction="right"):
        """Release the Ghost in a random direction."""
        if direction == "up":
            velocity = Point(0, -GHOST_VELOCITY)
            self._animation = self._animations[DIR_UP]
        elif direction == "right":
            velocity = Point(GHOST_VELOCITY, 0)
            self._animation = self._animations[DIR_RIGHT]
        elif direction == "down":
            velocity = Point(0, GHOST_VELOCITY)
            self._animation = self._animations[DIR_DOWN]
        elif direction == "left":
            velocity = Point(-GHOST_VELOCITY, 0)
            self._animation = self._animations[DIR_LEFT]
            
        self._body.set_velocity(velocity)
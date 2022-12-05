from random import randint 
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ghost(Actor):
    """A player that moves around in the game and interacts with PacMan."""
    
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
        self._direction = "s"
    
    def get_animation(self):
        """Gets the ghost's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def swing_up(self):
        """Steers the ghost up."""
        velocity = Point(0, -GHOST_VELOCITY)
        self._direction = "u"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_UP]

    def swing_right(self):
        """Steers the ghost right."""
        velocity = Point(GHOST_VELOCITY, 0)
        self._direction = "r"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_RIGHT]

    def swing_down(self):
        """Steers the ghost down."""
        velocity = Point(0, GHOST_VELOCITY)
        self._direction = "d"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_DOWN]
        
    def swing_left(self):
        """Steers the ghost left."""
        velocity = Point(-GHOST_VELOCITY, 0)
        self._direction = "l"
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
    
    def get_direction(self):
        """Gets the direction of the Ghost.
        
        Returns:
            A string describing the direction of the Ghost.
        """
        return self._direction
    
    def set_direction(self, direction):
        """Sets the direction of the Ghost."""
        self._direction = direction

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

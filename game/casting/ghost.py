from random import randint 
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ghost(Actor):
    """A player that moves around in the game and interacts with PacMan."""
    
    def __init__(self, body, name, animation, debug = False):
        """Constructs a new Ghost.

        Args:
            body: A new instance of Body.
            animation: A list containing the animation objects. 
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animations = animation
        self._name = name
        self._animation = self._animations[0]
        self._direction = "s"
        self._state = "g"

    def get_name(self):
        """Gets the name of ghost.
        
        Returns:
            The name of the ghost
        """
        return self._name
    
    def set_name(self, name):
        """Sets the name of the ghost.
        
        Args:
            name: The name of the ghost.
        """
        self._name = name
    
    def get_animation(self):
        """Gets the ghost's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation
    
    def set_animation(self, animation):
        """Sets the ghost's animation.
        
        Args:
            animation: A list containing the new animation objects. 
        """
        self._animations = animation

    def get_state(self):
        """Gets the state of the ghost.
        
        Returns:
            The state of the ghost. (g: ghost, e:eye/dead)
        """

        return self._state
    
    def set_state(self, state):
        """Sets the sate of the ghost.
        
        Args:
            state: The state of the ghost. (g: ghost, e:eye/dead). 
        """
        self._state = state

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
        """Gets the ghost's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ghost's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
    
    def get_direction(self):
        """Gets the direction of the ghost.
        
        Returns:
            A string describing the direction of the ghost.
        """
        return self._direction
    
    def set_direction(self, direction):
        """Sets the direction of the ghost."""
        self._direction = direction

    def release(self, direction=""):
        """Release the Ghost in a given direction."""
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
        else: 
            velocity = self._body.get_velocity()
            self._animation = self._animations[DIR_RIGHT]
            
        self._body.set_velocity(velocity)

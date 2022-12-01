from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Racket(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animations = animation
        self._animation = self._animations[DIR_RIGHT]

    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_up(self):
        """Moves PacMan up."""
        velocity = Point(0, -PACMAN_VELOCITY)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_UP]

    def move_right(self):
        """Moves PacMan right."""
        velocity = Point(PACMAN_VELOCITY, 0)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_RIGHT]

    def move_down(self):
        """Moves PacMan down."""
        velocity = Point(0, PACMAN_VELOCITY)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_DOWN]
        
    def move_left(self):
        """Moves PacMan left."""
        velocity = Point(-PACMAN_VELOCITY, 0)
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_LEFT]
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
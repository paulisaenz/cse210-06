from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Pacman(Actor):
    """The main character of the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new PacMan.
        
        Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animations = animation
        self._animation = self._animations[DIR_RIGHT]
        self._direction = "right"

    def get_animation(self):
        """Gets PacMan's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets PacMan's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves PacMan using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers PacMan to the left."""
        velocity = Point(-PACMAN_VELOCITY, 0)
        self._direction = "left"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_LEFT]
        
    def swing_right(self):
        """Steers PacMan to the right."""
        velocity = Point(PACMAN_VELOCITY, 0)
        self._direction = "right"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_RIGHT]

    def swing_up(self):
        """Steers PacMan up."""
        velocity = Point(0, -PACMAN_VELOCITY)
        self._direction = "up"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_UP]

    def swing_down(self):
        """Steers PacMan down."""
        velocity = Point(0, PACMAN_VELOCITY)
        self._direction = "down"
        self._body.set_velocity(velocity)
        self._animation = self._animations[DIR_DOWN]
    

    def stop_moving(self):
        """Stops PacMan from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)

    def get_direction(self):
        """Gets the direction of the PacMan.
        
        Returns:
            A string describing the direction of the PacMan.
        """
        return self._direction
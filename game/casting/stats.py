from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.
        #Returns:
            #A number representing the level.
        #"""
        return self._level

    def get_lives(self):
        """Gets the lives.
        Returns:
            A number representing the lives.
        """
        return self._lives
    
    def update_lives(self):
        """Update PacMan lives when they encounter a ghost.
        """
        return self.update_lives
  
    def get_score(self):
        """Gets the score.
        Returns:
            A number representing the score.
        """
        #if pacman eats cherry 
            #then self.score += 100

        return self._score

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1 #if pacman touches ghost then loses one life 

        return self.update_lives #or self.lives 
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
from game.casting.actor import Actor


class Path(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, directions, debug = False):
        """Constructs a new Wall.
        
        Args:
            body: A new instance of Body.
            directions: List of possible directions to take.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._directions = directions

    def get_body(self):
        """Gets the paths's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
    
    def get_directions(self):
        """Gets the path's directions.
        
        Returns:
            List of directions.
        """
        return self._directions
from game.casting.actor import Actor


class Cherry(Actor):
    """An object to engage with PacMan."""

    def __init__(self, body, image, points, debug = False):
        """Constructs a new cherry.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            points: The number of points the cherry is worth
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points

    def get_image(self):
        """Gets the cherry image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the cherry body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the cherry points.
        
        Returns:
            A number representing the cherry's points.
        """
        return self._points

    

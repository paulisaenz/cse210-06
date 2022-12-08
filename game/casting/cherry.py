from random import randint 
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Cherry(Actor):
    """
    Responsibility: Exist as an actor, and add to the score when touched
    Specifics -
        Make a method that takes the current score, adds one to it, and returns the new score
    """

    def __init__(self):
        super().__init__(self)
        self.images = []
        for i in range(1, 5):
            img = ('images' + 'cherries' + str(i) + '.png').convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

            cherries = Cherry() 
            cherries.rect.x = 0
            cherries.rect.y = 0



    #def get_score(self):
        #return self.new_score

    #def add_score(self, score):
        #return score + 100

    

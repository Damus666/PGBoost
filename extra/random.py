import random
from noinit import _NoInit
from extra.math import Math
from typing import Iterable,Any

class Random(_NoInit):
    """Groups python 'random' module into a class with some additional ones"""
    
    RangeInt=random.randint
    Range = random.randrange
    RangeFloat = random.uniform
    Choice = random.choice
    Choices = random.choices
    Seed = random.seed
    Shuffle = random.shuffle
    Bytes = random.randbytes
    
    @staticmethod
    def WeightedChoice(sequence:Iterable[Any],weights:Iterable[int])->Any:
        """Uses weights to return a random value from a sequence using probability"""
        weightssum = sum(weights)
        chosen = Random.RangeInt(0,weightssum)
        cweight = 0
        i = 0
        for w in weights:
            if Math.InsideEqualRange(chosen,cweight,cweight+w):
                return sequence[i]
            cweight += w
            i += 1
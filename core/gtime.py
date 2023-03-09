import pygame,time
from noinit import _NoInit

onediv1000 = 1/1000

class Time(_NoInit):
    """Contains time info updated internally"""
    time:float = 0
    deltaTime:float = 0
    ticks:float = 0
    frameCount:float = 0
    frameRate:float = 0
    desiredFrameRate:int = 0
    timeScale:float = 1
    _clock:pygame.time.Clock = None
    
    @property
    def sysTime(self)->float:
        return time.time()
    
    @classmethod
    def _init(cls,frameRate):
        cls._clock = pygame.time.Clock()
        cls.desiredFrameRate = frameRate
        
    @classmethod
    def _update(cls):
        cls.deltaTime = cls._clock.tick(cls.desiredFrameRate)*onediv1000*cls.timeScale
        cls.ticks = pygame.time.get_ticks()
        cls.time = cls.ticks*onediv1000
        cls.frameCount += 1
        cls.frameRate = cls._clock.get_fps()
        
    def DelayMS(milliseconds:float)->float:
        """Stops the application for some time"""
        return pygame.time.delay(milliseconds)
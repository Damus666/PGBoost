import pygame
from ..elements.skybox import SkyboxType
from ..noinit import _NoInit

class InitSettings(_NoInit):
    """The application will use this settings to initialize the core components"""
    desiredFrameRate:int=60
    sizes:tuple[int,int]=(1920,1080)
    flags:int = 0
    title:str = "Pygame Window (With Pygame Boost)"
    vsync:bool = False
    skyboxType:SkyboxType = SkyboxType.Color
    skyboxValue:str|tuple = "black"
    inputMovementElasticity:float = 0.05
    cameraZoomRange:pygame.Vector2 = pygame.Vector2(0.001,100)
    
    @classmethod
    def Change(cls,**attributes):
        """Change any init setting with keyword arguments"""
        for name,value in attributes.items():
            setattr(cls,name,value)
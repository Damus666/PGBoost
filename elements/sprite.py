import pygame
from ..noinit import _NoInit
from warnings import warn

from pygame.sprite import Sprite
from pygame.sprite import Group as SpriteGroup
from pygame.sprite import GroupSingle as SpriteGroupSingle
from pygame.sprite import spritecollide as SpriteCollide
from pygame.sprite import spritecollideany as SpriteCollideAny

class SpriteManager(_NoInit):
    """Contains all the surfaces. An empty surface is loaded from 'assets/default/empty.png' as 'none'/'empty'"""
    sprites:dict[str,pygame.Surface] = dict()
    
    @classmethod
    def _init(cls):
        try:
            s = cls.Add("none","assets/default/empty.png")
            cls.sprites["empty"] = s
        except:
            warn("Failed to load 'empty.png' from 'assets/default/empty.png'. Considering adding that file to your project to have the 'none/empty' sprite available",ResourceWarning)
    
    @classmethod
    def Add(cls,name:str,path:str,scalefactor:tuple[float,float]=None,sizes:tuple[int,int]=None,convert_alpha=False)->pygame.Surface:
        """Add a new surface to the dictionary and return it"""
        if convert_alpha:
            surface = pygame.image.load(path).convert_alpha()
        else:
            surface = pygame.image.load(path).convert()
        if scalefactor != None:
            w,h = surface.get_width(),surface.get_height()
            surface = pygame.transform.scale(surface,(w*scalefactor[0],h*scalefactor[1]))
        elif sizes != None:
            surface = pygame.transform.scale(surface,sizes)
        cls.sprites[name] = surface
        return surface
        
    @classmethod
    def Get(cls,name)->pygame.Surface:
        """Return the surface with a name"""
        return cls.sprites[name]
    

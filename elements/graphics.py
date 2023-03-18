import pygame
from typing import Any
from ..noinit import _NoInit

class Graphics(_NoInit):
    """Groups pygame 'draw', 'transform' and 'image' module in a class with some additional methods"""
    Circle = pygame.draw.circle
    Rect = pygame.draw.rect
    Line = pygame.draw.line
    Lines = pygame.draw.lines
    Polygon = pygame.draw.polygon
    AALine = pygame.draw.aaline
    AALines = pygame.draw.aalines
    Arc = pygame.draw.arc
    Ellipse = pygame.draw.ellipse
    
    Scale2x = pygame.transform.scale2x
    Rotate = pygame.transform.rotate
    Rotozoom = pygame.transform.rotozoom
    Flip = pygame.transform.flip
    Chop = pygame.transform.chop
    
    Save = pygame.image.save
    Surface = pygame.Surface
    Load = pygame.image.load
    
    @classmethod
    def EmptySurface(cls,sizes,color=None):
        s = cls.Surface(sizes)
        if color:
            s.fill(color)
        return s
    
    @staticmethod
    def Scale(surface:pygame.Surface,sizes:tuple[int|float,int|float],smooth:bool=False,dest_surf:pygame.Surface=None)->pygame.Surface:
        """Changes a surface sizes"""
        if smooth:
            return pygame.transform.smoothscale(surface,(int(sizes[0]),int(sizes[1])),dest_surf)
        return pygame.transform.scale(surface,sizes,dest_surf)
    
    @staticmethod
    def ScaleBy(surface:pygame.Surface,factor:tuple[float,float],smooth:bool=False,dest_surf:pygame.Surface=None)->pygame.Surface:
        """Scale a surface multiplying the width and height by a factor"""
        w = surface.get_width()
        h = surface.get_height()
        if smooth:
            return pygame.transform.smoothscale(surface,(int(w*factor[0]),int(h*factor[1])),dest_surf)
        return pygame.transform.scale(surface,(int(w*factor[0]),int(h*factor[1])))
    
    @staticmethod
    def SurfaceData(surface:pygame.Surface)->dict[str,Any]:
        """Get common surface info in a dictionary (width, height, alpha, flags, masks)"""
        return {
            "width":surface.get_width(),
            "height":surface.get_height(),
            "alpha":surface.get_alpha(),
            "flags":surface.get_flags(),
            "masks":surface.get_masks()
        }
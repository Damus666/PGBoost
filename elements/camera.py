import pygame
from core.window import Window
from noinit import _NoInit
from core.input import Input
from elements.graphics import Graphics
from typing import SupportsIndex,Iterable

class Camera(_NoInit):
    """Contains camera position, zoom and methods"""
    position:pygame.math.Vector2 = pygame.math.Vector2()
    zoom:float = 1
    zoomRange:pygame.Vector2 = pygame.Vector2()
    
    @classmethod
    def _init(self,zoomrange):
        self.zoomRange = zoomrange
            
    @classmethod
    def UpdateZoom(self,amount:float):
        """Updates the zoom clamping it in the range"""
        self.zoom = max(self.zoomRange.x,min(self.zoom+amount,self.zoomRange.y))
    
    @classmethod
    def SetZoom(self,zoom:float):
        """Sets the zoom clamping it in the range"""
        self.zoom = max(self.zoomRange.x,min(zoom,self.zoomRange.y))
    
    @classmethod    
    def _left(self):
        return self.position.x-Window.center.x
    
    @classmethod
    def _top(self):
        return self.position.y-Window.center.y

    @classmethod
    def ScreenToWorld(self,point:SupportsIndex)->pygame.Vector2:
        """Project a point on the screen to a point in the world."""
        return pygame.Vector2(((point[0]/self.zoom)+self.left()),((point[1]/self.zoom)+self.top()))
    
    @classmethod
    def WorldToScreen(self,point:SupportsIndex)->pygame.Vector2:
        """Inverse of 'ScreenToWorld'."""
        return pygame.Vector2(((point[0]/self.zoom)-self.left()),((point[1]/self.zoom)-self.top()))

    @classmethod
    def left(self)->float:
        """Returns the left camera border"""
        return self.position.x - (Window.sizes.x/self.zoom)*0.5
    
    @classmethod
    def right(self)->float:
        """Returns the right camera border"""
        return self.position.x + (Window.sizes.x/self.zoom)*0.5
    
    @classmethod
    def top(self)->float:
        """Returns the top camera border"""
        return self.position.y - (Window.sizes.y/self.zoom)*0.5
    
    @classmethod
    def bottom(self)->float:
        """Returns the bottom camera border"""
        return self.position.x + (Window.sizes.y/self.zoom)*0.5
    
    @classmethod
    def Drag(cls,buttons:Iterable=[0,1,2]):
        """Drags the camera using the mouse"""
        for btn in buttons:
            if Input.pressedMouse[btn]:
                cls.position -= Input.mouseRelative/cls.zoom
                break
            
    @classmethod
    def Zoom(cls,speed:float=0.1)->bool:
        """Zooms the camera using the mouse wheel. Returns wether the zoom changed or not"""
        val = Input.mouseWheelRel.y*speed*cls.zoom
        cls.UpdateZoom(val)
        return val != 0
        
    @classmethod
    def Project(cls,position:SupportsIndex)->pygame.Vector2:
        """Projects a world position to the camera space, to render objects in the right place"""
        dx = position[0]-cls.position.x
        dy = position[1]-cls.position.y
        x = ((position[0]-cls._left())+((dx*cls.zoom)-dx))
        y = ((position[1]-cls._top())+((dy*cls.zoom)-dy))
        return pygame.Vector2(x,y)
    
    @classmethod
    def ZoomSurface(cls,surface):
        """Scales a surface using the camera zoom"""
        return Graphics.ScaleBy(surface,(cls.zoom,cls.zoom))
import pygame
from ..noinit import _NoInit

class WindowFlag(_NoInit):
    """Pygame window flags grouped in a class. Pygame constants are fine too"""
    Resizable = pygame.RESIZABLE
    Fullscreen = pygame.FULLSCREEN
    Doublebuffer = pygame.DOUBLEBUF
    Noframe = pygame.NOFRAME
    Noevent = pygame.NOEVENT
    Hidden = pygame.HIDDEN
    Shown = pygame.SHOWN

class Window(_NoInit):
    """Contain window data and modification methods"""
    sizes:pygame.math.Vector2 = pygame.math.Vector2(0,0)
    center:pygame.math.Vector2 = pygame.Vector2(0,0)
    title:str = ""
    vsync:bool = False
    surface:pygame.Surface = None
    flags:int = 0
    _sizeschangeevent = list()
    rect:pygame.Rect = None
    Blit = None
    Fill = None
    Blits = None
    
    @classmethod
    def _init(cls,sizes,title,flags,vsync):
        cls.sizes = pygame.math.Vector2(sizes)
        cls.center = pygame.math.Vector2(cls.sizes[0]/2,cls.sizes[1]/2)
        cls.title = title
        cls.vsync = vsync
        cls._flags = flags
        cls.surface = pygame.display.set_mode((sizes[0],sizes[1]),flags,vsync=vsync)
        cls.Blit = cls.surface.blit
        cls.Blits = cls.surface.blits
        cls.Fill = cls.surface.fill
        cls.rect = cls.surface.get_rect()
        pygame.display.set_caption(title)
        
    @classmethod
    def ChangeTitle(cls,new:str):
        """Change the window title"""
        cls.title = new
        pygame.display.set_caption(new)
        
    @classmethod
    def ChangeDimentions(cls,new:tuple[int,int]):
        """Change the window sizes"""
        if (new != cls.sizes):
            cls.center = pygame.math.Vector2(cls.sizes[0]/2,cls.sizes[1]/2)
            for el in cls._sizeschangeevent:
                try:
                    el()
                except: pass
        cls.sizes = pygame.math.Vector2(new)
        cls.surface = pygame.display.set_mode((new[0],new[1]),cls.flags,vsync=int(cls.vsync))
        cls.Blit = cls.surface.blit
        cls.Blits = cls.surface.blits
        cls.Fill = cls.surface.fill
        cls.rect = cls.surface.get_rect()
        
    @classmethod
    def ChangeFlags(cls,new:int):
        """Change the window flags and rebuild it"""
        cls.flags = new
        cls.ChangeDimentions(cls.sizes)
        
    @classmethod
    def ChangeVsync(cls,new:bool):
        """Change the mode to vsync or not"""
        cls.vsync = new
        cls.ChangeDimentions(cls.sizes)
        
    _update = pygame.display.update
        
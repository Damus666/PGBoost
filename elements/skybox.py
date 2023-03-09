import pygame,typing
from .sprite import SpriteManager
from core.window import Window
from noinit import _NoInit

class SkyboxType(_NoInit):
    """Available types are 'Color' and 'Image'"""
    Color = 0
    Image = 1
    
class Skybox(_NoInit):
    """Contains data on how to fill the background"""
    type:SkyboxType = SkyboxType.Color
    color:str|tuple = (0,0,0)
    sprite:pygame.Surface = None
    scaledSprite:pygame.Surface = None
    
    @classmethod
    def _init(self,type:SkyboxType,color_or_spritename:str|typing.Any):
        if type == SkyboxType.Color:
            self.color = color_or_spritename
        elif type == SkyboxType.Image:
            self.sprite = SpriteManager.get(color_or_spritename)
            Window._sizeschangeevent.append(self._rescale_sprite)
            self._rescale_sprite()
        else:
            raise Exception("Allowed types are Color and Image")
            
    def _rescale_sprite(self):
        self.scaledSprite = pygame.transform.scale(self.sprite,Window.sizes)
    
    @classmethod
    def ChangeSprite(self,name:str):
        """Change the skybox background image"""
        self.sprite = SpriteManager.get(name)
        self._rescale_sprite()
    
    @classmethod
    def _render(self):
        if self.sprite:
            Window.surface.blit(self.scaledSprite,(0,0))
        else:
            Window.surface.fill(self.color)
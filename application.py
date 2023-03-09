# builtins
import pygame,sys
# core
from core.gtime import Time
from core.input import Input,KeyCode
from core.window import Window
from core.settings import InitSettings
from core.game import Game
# elements
from elements.skybox import SkyboxType,Skybox
from elements.camera import Camera
from elements.sprite import SpriteManager
from elements.timers import TimerManager,Timer,CooldownTimer
# ui
from ui.ui import UI
# noinit
from noinit import _NoInit

class Application(_NoInit):
    """
    Main application class. Init must be called before Run\n\n
    By convention methods and fields starting with '_' should not be used by the user
    """
    
    @staticmethod
    def Init():
        """Init pygame, Window, Time, Input, SpriteManager, Skybox, Camera using InitSettings"""
        pygame.init()
        Window._init(InitSettings.sizes,InitSettings.title,InitSettings.flags,InitSettings.vsync)
        Time._init(InitSettings.desiredFrameRate)
        Input._init(InitSettings.inputMovementElasticity)
        SpriteManager._init()
        Skybox._init(InitSettings.skyboxType,InitSettings.skyboxValue)
        Camera._init(InitSettings.cameraZoomRange)
        
    @staticmethod
    def Quit(game:Game=None):
        """Quit the application at any time. If 'game' is given, Game.Quit is called"""
        canquit = True
        if game:
            stopquit = game.Quit()
            if stopquit == True:
                canquit = False
        if canquit:
            pygame.quit()
            sys.exit()
        
    @staticmethod
    def Run(game:Game):
        """
        Starts the game loop. 'game' methods will be called as described in their __doc__\n\n
        
        Loop structure:\n
            Time update\n
            Input update\n
            event loop:\n
                quit event\n
                Input event\n
                UI event\n
            Timers update\n
            Game update\n
            UI update\n
            Skybox render\n
            Game draw\n
            UI draw\n
            Game late update\n
            Window update\n
        
        """
        if not pygame.get_init():
            raise Exception("Application.init() must be called before starting the game")
        game.Start()
        while True:
            Time._update()
            Input._update()
            events = pygame.event.get()
            Input.frameEvents = events
            for e in events:
                if e.type == pygame.QUIT:
                    Application.Quit(game)
                Input._event(e)
                UI._event(e)
            TimerManager._update()
            game.Update()
            UI._update()
            Skybox._render()
            game.Draw()
            UI._draw()
            game.LateUpdate()
            Window._update()
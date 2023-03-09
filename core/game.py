class Game:
    """Contains overridable functions used by the main loop"""
    
    def Start(self):
        """'Start' is called just before the loop starts"""
        pass
    
    def Update(self):
        """'Update' is called after the internal update, event loop and timers update and before the UI update"""
        pass
    
    def Draw(self):
        """'Draw' is called after the skybox rendering and before the UI rendering"""
        pass
    
    def LateUpdate(self):
        """'LateUpdate' is called after all updates and rendering and before the window display update"""
        pass
    
    def Quit(self)->bool:
        """'Quit' is called before the application quits. If 'True' is returned, the application will not quit"""
        return False
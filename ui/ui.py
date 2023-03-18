from ..ui.pygameUI import UIManager
from ..core.window import Window
from ..noinit import _NoInit

class UI(_NoInit):
    """Wrapper for the library 'pygameUI'. The libray is a seprate project with a different naming convention"""
    
    managers:list[UIManager] = list()
    manager:UIManager = None
    
    @classmethod
    def AddManager(cls,manager:UIManager,active=False):
        """Adds a 'UIManager' to the list and returns it"""
        cls.managers.append(manager)
        if active:
            cls.SetManager(manager)
        return manager
        
    @classmethod
    def SetManager(cls,manager:UIManager):
        """Set a 'UIManager' as the current"""
        cls.manager = manager
        return manager
        
    @classmethod
    def SetManagerIndex(cls,index:int):
        """Set a 'UIManager' as the current from an index"""
        m = cls.managers[index]
        cls.manager = m
        return m
        
    @classmethod
    def _event(cls,e):
        if cls.manager:
            cls.manager.handle_events(e)
            
    @classmethod
    def _update(cls):
        if cls.manager:
            cls.manager.update_ui(1)
            
    @classmethod
    def _draw(cls):
        if cls.manager:
            cls.manager.draw_ui(Window.surface)
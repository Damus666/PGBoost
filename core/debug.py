import os
from typing import Callable,Any
from ..noinit import _NoInit

class Debug(_NoInit):
    _clear_console_command = "cls"
    _collapse = True
    _logs:list|dict = {}
    Print = print
    
    @classmethod
    def Count(cls,element:object):
        """Returns how many times an element occurs in the logs"""
        if cls._collapse:
            return cls._logs[str(element)]
        else:
            return cls._logs.count(str(element))
    
    @classmethod
    def Log(cls,*elements:object):
        """Add an element to the logs. Depending on the 'collapse' flag, the duplicates will be combined."""
        for element in elements:
            el = str(element)
            if cls._collapse:
                if el in cls._logs.keys():
                    cls._logs[el] += 1
                else:
                    cls._logs[el] = 1
            else:
                cls._logs.append(el)
        cls.Refresh()
    
    @classmethod
    def ClearConsole(cls):
        """Clear the console with the command provided in 'setup'. Done automatically"""
        os.system(cls._clear_console_command)
    
    @classmethod
    def ClearLogs(cls):
        """Clear the logs"""
        cls._logs.clear()
        cls.Refresh()
    
    @classmethod
    def PrintLogs(cls):
        """Print the logs to the console. Done automatically"""
        l = [k+f" ({v})" if v >= 2 else k for k,v in cls._logs.items()] if cls._collapse else cls._logs
        print("\n".join(l))
    
    @classmethod
    def Remove(cls,*elements:object,all:bool=True):
        """Remove elements from the log. Depending on the 'collapse' and 'all' flags, only one or all occurrences of the element will be removed"""
        for element in elements:
            el = str(element)
            if cls._collapse:
                if el in cls._logs.keys():
                    amount = cls._logs[el]
                    if amount <= 1 or all:
                        del cls._logs[el]
                    else:
                        cls._logs[el] -= 1
            else:
                if all:
                    cls._logs = list(filter((el).__ne__, cls._logs))
                else:
                    if el in cls._logs:
                        cls._logs.remove(el)
        cls.Refresh()
    
    @classmethod
    def Refresh(cls):
        """Refreshes the console with the logs. Done automatically"""
        cls.ClearConsole()
        cls.PrintLogs()
    
    @classmethod
    def Setup(cls,clear_console_command:str="cls",collapse:bool=True):
        """Changes the console clear command and the collapse flag, refreshing the logs"""
        cls._clear_console_command = clear_console_command
        old = cls._collapse
        cls._collapse = collapse
        if cls._collapse:
            if old:
                return
            oldl = cls._logs.copy()
            cls._logs = {}
            cls._log(*oldl)
        else:
            if not old:
                return
            oldl = cls._logs.copy()
            cls._logs = list()
            for k,v in oldl.items():
                for i in range(v):
                    cls._logs.append(k)
        cls.Refresh()

    @staticmethod
    def Join(*elements:object,sep:str=", ")->str:
        """Joins objects with the separator"""
        return sep.join(map(str,elements))

    @staticmethod
    def Debug(pre:Callable[[],Any]=None,post:Callable[[],Any]=None)->Callable:
        """Decorator to log a string before and/or after the execution of the function. the strings are given by the 'pre' and 'post' that must be callable"""
        def decorator(func):
            def wrapper(*args,**kwargs):
                if pre:
                    Debug.Log(pre())
                val = func(*args,**kwargs)
                if post:
                    Debug.Log(post())
                return val
            return wrapper
        return decorator
    

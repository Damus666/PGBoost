from inspect import isfunction
import warnings
from typing import Type, Any

class Table:
    """
    Object representing a table inspired by lua
    
    Constructor (example):\n
    \n
    Table(
        variable = value,\n
        another = value
    )\n
    \n
    Special Arguments:\n
    \n
    def prefix_example_function(self):
        print(self.variable)\n
    \n
    t = Table(
        prefix = "prefix_",\n
        functions = [prefix_example_function]
    )\n
    \n
    t.example_function() # >>> variable\n
    \n
    using "functions" instead of a normal kwarg assures the function will receive the "self"\n
    using "prefix" will let you add a prefix to the functions that will be removed in the object attribute\n
    \n
    Special Functions:\n
    \n
    user can provide the functions: 'main', 'string', 'repr'\n
    main -> called when the table is called\n
    string -> called when str(table) is called\n
    repr -> called when repr(table) is called\n
    \n
    Notes:\n
    if the user tries to get a non existent variable, None is returned and a warning is raised
    """
    def __init__(self,**attributes):
        self.__call = None
        self.__str = None
        self.__repr = None
        self.super = self
        
        def handle_special(name,value):
            if name == "main":
                self.__call = _TableFunction(value,self); return True
            if name == "string":
                self.__str = _TableFunction(value,self); return True
            if name == "repr":
                self.__repr = _TableFunction(value,self); return True
            return False
        
        prefix = ""
        
        for name,value in attributes.items():
            if name == "prefix":
                prefix = value
                continue
            if name == "functions":
                if not hasattr(value,"__iter__"):
                    raise TypeError(f"Cannot get functions from non-iterable {type(value)}")
                for function in value:
                    if not callable(function):
                        raise TypeError(f"'{function.__name__}' must be callable")
                    
                    if handle_special(function.__name__.removeprefix(prefix),function): continue
                    setattr(self,function.__name__.removeprefix(prefix),_TableFunction(function,self))
                    
                continue
            
            setattr(self,name,value)
            
    def __setitem__(self,index,value):
        self.__dict__[index] = value
        
    def __getitem__(self,index):
        return self.__dict__[index]
    
    def __call__(self, *args, **kwargs):
        if self.__call:
            return self.__call(*args,**kwargs)
        
    def __str__(self):
        if self.__str:
            return self.__str()
        return f"Table{vars(self).keys()}"
    
    def __repr__(self):
        if self.__repr:
            return self.__repr()
        return f"Table{vars(self)}"
    
    def __setattr__(self, __name: str, __value) -> None:
        if isfunction(__value) and __value.__code__.co_varnames[0] in ["self","this"] and not isinstance(__value,_TableFunction):
            self.__dict__[__name]=_TableFunction(__value,self)
            return
        self.__dict__[__name] = __value
        
    def __getattr__(self,name):
        msg = "Trying to access a non-existent attribute of a table"
        warnings.warn(msg,Warning)
        return None
    
    def Inherit(self,table):
        """
        Iterates the table variables and if the current table does not have them, it adds them to it\n
        Variables are not deepcopied\n
        Functions will receive the correct 'self' instance\n
        The original table is returned
        """
        if not isinstance(table,Table):
            raise TypeError("Table argument must be of type 'table'")
        tablevars = vars(table)
        myvars = vars(self)
        for name,value in tablevars.items():
            if name not in myvars.keys():
                if not isinstance(value,_TableFunction):
                    setattr(self,name,value)
                else:
                    setattr(self,name,_TableFunction(value._TableFunction__func,self))
        if not self.__call:
            if table._Table__call:
                self.__call = _TableFunction(table._Table__call._TableFunction__func,self)
        if not self.__str:
            if table._Table__str:
                self.__str = _TableFunction(table._Table__str._TableFunction__func,self)
        if not self.__repr:
            if table._Table__repr:
                self.__repr = _TableFunction(table._Table__repr._TableFunction__func,self)
        self.super = table
        return self
    
class _TableFunction:
    """
    Makes it possible for table functions to be given the 'self' argument.\n
    Internal
    """
    def __init__(self,func,table):
        self.__func = func
        self.__table = table
        
    def __call__(self,*args,**kwargs):
        return self.__func(self.__table,*args,**kwargs)

class _FromImport:
    def __init__(self,obj):
        self.__obj = obj
        
    def Import(self,*names:str)->list[Any]:
        """Return a list with the values from the object provided in 'From'"""
        vs = []
        for name in names:
            v = getattr(self.__obj,name)
            vs.append(v)
        return vs

def From(obj:object|Type)->_FromImport:
    """Lets you import fields and methods from classes"""
    return _FromImport(obj)

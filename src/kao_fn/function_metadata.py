from .smart_arg import SmartArg
import inspect

class FunctionMetadata:
    """ Represents a functions metadata """
    
    def __init__(self, func):
        """ Initialize the metadata """
        args, varargs, keywords, defaults = inspect.getargspec(func)
        
        self.argNameToIndex = {arg:args.index(arg) for arg in args}
        self.nameToDefaultValue = dict(zip(reversed(args), reversed(defaults))) if defaults is not None else {}
        
        self.args = [SmartArg(arg, self.argNameToIndex[arg]) for arg in args]
        self.nameToArg = {arg.argName:arg for arg in self.args}
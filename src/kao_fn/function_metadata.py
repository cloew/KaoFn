from .smart_arg import SmartArg
import inspect

class FunctionMetadata:
    """ Represents a functions metadata """
    
    def __init__(self, func):
        """ Initialize the metadata """
        args, varargs, keywords, defaults = inspect.getargspec(func)
        self.argToIndex = {arg:args.index(arg) for arg in args}
        self.nameToDefaultValue = dict(zip(reversed(args), reversed(defaults)))
        self.nameToArg = {arg:SmartArg(arg, self.argToIndex[arg]) for arg in args}
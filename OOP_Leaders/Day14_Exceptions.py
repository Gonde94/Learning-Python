"""
An exception is an error that is detected while a program is being executed.
Built-in exceptions include ValueError or TypeError. 

When creating a module, it may be useful to create custom Exception classes that are
more specific than generic Python exceptions. 
They should be derived from the Exception class.
"""


class MySpecificError(Exception):
    pass

# Or subclassing a specific exception
class MySpecificError(ValueError):
    pass

# Perhaps a built-in error is sufficient 
#class General:
#    def __init__(self, birthyear):
#        self.birthyear = birthyear

#        if type(self.birthyear) is not int:
#            raise TypeError("The birthyear should be an integer.")
    

if __name__ == "__main__":

    pass

    #Rommel = General("1891") 
    # # raises TypeError

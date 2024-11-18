"""
We have seen child classes (Prophet, Dictator) inherit from a parent class (Leader).
Sometimes, simple inheritance is not enough.

Abstract Base Classes are useful if a hierarchy of classes are involved. They:
1) Let a parent class communicate that subclasses should have a certain structure.
2) Allow classes to identify themselves as meeting those demanded requirements.
3) Enforce that a subclass meets requirements, otherwise throwing an exception
at instantiation time.

An abstract method is one that has a declaration but not an implementation. This method
is then overriden by the subclasses.

I will implement an idea taken from CIV. Different types of "Victory" exist - domination,
scientific, cultural, diplomatic. So the Victory class can be an application for the
abc module. 

Every type of victory has a name and a method. Each victory subclas will have a defining
feature and a ...
"""

from abc import ABC, abstractmethod

class Victory(ABC):
    """ Creates a type of victory. """

    def __init__(self, name: str, method: str, difficulty: int):
        self.name = name
        self.method = method
        self.difficulty = difficulty

    # Notice the two abstract methods below with a declaration but no implementation.
    # Also when stacking decorators, they are implemented bottom to top.
    # Abstract method should be the innermost decorator.

    @abstractmethod
    def cast(self):
        pass 

    @property
    @abstractmethod
    def check_conditions(self):
        pass

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self.name}', method='{self.method}'")
    

class Domination(Victory):
    def __init__(self, name: str, method: str, difficulty: int = 10):
        super().__init__(name, method, difficulty)

    @property
    def check_conditions(self) -> str:
        return ("Checking if all capitals have been taken from their players.")

    def winning_move(self):
        return ("Capture the last player's capital city.")


class Science(Victory):
    def __init__(self, name: str, method: str, difficulty: int = 7):
        super().__init__(name, method, difficulty)

    @property
    def check_conditions(self) -> str:
        return ("Checking if player has built a spaceship.")
    
    def cast(self):
        return ("Launch spaceship in 10 moves.")


if __name__ == "__main__":
    
    #diplomatic = Victory(name="Diplomatic", 
    #                     method="Winning a majority vote in the UN.",
    #                     difficulty=9)
    #print(diplomatic) 
    # This does not work as cannot instantiate an abstract base class

    science = Science(name="Science",
                      method="Build and launch a spaceship.")
    print(science)
    print(science.difficulty)

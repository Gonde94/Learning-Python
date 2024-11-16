"""
We can control how instances of our classes are converted into string objects through two methods.

The purpose of __repr__ is to aid debugging for developers and so should be as unambiguous as possible.
It returns a representation of the instance that can be used to recreate it.

The result of __str__ should be readable, i.e. how the object should look like to a user, not developer.

Python starts by looking for the __str__ method. If it doesn't find it, it falls back on __repr__.
Subclasses inherit parent class methods, but we should give each their own to avoid ambiguity. 

Also adding type annotations.
"""

class Leader:
    """
    Creates a leader.
    """

    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
    

if __name__ == "__main__":

    MLK = Leader("Martin Luther King", "USA")
    print(MLK)
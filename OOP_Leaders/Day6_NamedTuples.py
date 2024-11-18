"""
Namedtuples are an extension of tuples. They allow us to name the field of a tuple.
This makes it easier to access the individual fields and makes the code more readable.

typing.NamedTuple allows us to specify each type of field and come with an implementation
of __repr__ so we don't have to add this manually for the objects.
"""

from collections import namedtuple
from typing import NamedTuple

# Example 1 with collections.namedtuple
Pet = namedtuple("Pet", ["name", "type"])
Dorothys_pet = Pet("Toto", "dog")


# Example 2 with typing.NamedTuple
class RomanArmyMember(NamedTuple):
    name: str
    birthyear: str

    @property
    def leader(self) -> "RomanArmyMember":
        caesar = RomanArmyMember("Julius Caesar", "100 BC")
        return caesar


if __name__ == "__main__":

    print(Dorothys_pet) # Pet(name='Toto', type='dog')
    print(Dorothys_pet.name) # Toto
    print(Dorothys_pet[1]) # dog

    africanus = RomanArmyMember("Scipio Africanus", "236 BC")
    print(africanus)
    print(africanus.leader) # Caesar's details

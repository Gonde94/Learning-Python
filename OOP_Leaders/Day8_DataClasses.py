"""
Data classes are mutable namedtuples with defaults. They do the same thing as
namedtuples but make it easier to create a class because they implement several
useful methods by default.

They typically mostly store values, but methods can also be added.
"""

from dataclasses import dataclass

@dataclass
class Empire:
    name: str
    leader: str
    founded_in: int
    collapsed_in: int
    area: int

    @property
    def calculate_age(self) -> int:
        return (f"{self.collapsed_in - self.founded_in} years")

# Above, python has automatically added special methods such as a __init__ and __repr__ method.


if __name__ == "__main__":

    mongol_empire = Empire(name="Mongol Empire",
                           leader="Genghis Khan",
                           founded_in=1206,
                           collapsed_in=1368,
                           area=23_500_000)
    print(mongol_empire)
    print(mongol_empire.calculate_age)
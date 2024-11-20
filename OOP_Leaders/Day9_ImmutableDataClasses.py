"""
We can make a dataclass immutable such that it fulfills the same purpose as typing.NamedTuple.
For this, we have to set frozen=True.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class SovietArmyMember():
    name: str
    birthyear: int

    @property
    def leader(self):
        zhukov = SovietArmyMember("Georgy Zhukov", 1896)
        return zhukov


if __name__ == "__main__":

    zoya = SovietArmyMember("Zoya Kosmodemyanskaya", 1923)
    print(zoya)
    print(zoya.leader)

    #zoya.name = "Anatoly Liapidevsky"
    # Frozen instance error: cannot assign to field 'name'
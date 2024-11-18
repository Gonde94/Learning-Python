"""
Class and static methods are good for communicating the intention one has in mind when 
implementing the method.

Class methods are bound to the class itself, not to instances of the class. 

A static method expresses that the method is independent from the rest of the class. They are
within the class for organisational purposes (but could still function if placed outside the class).
"""

from Day1_OOP import Leader


class Dictator(Leader):
    """
    Creates a dictator.
    """

    def __init__(self, name, country, years_in_power):
        super().__init__(name, country)
        self.years_in_power = years_in_power

        self._skills = {
            'Charisma': 0,
            'Oratory': 0,
            'Military strategy': 0,
            'Political savvy': 0,
            'Loyalty cultivation': 0
        }

    @staticmethod
    def calculate_reputation(years_in_power, wars_fought, enemies_killed):
        """ Determine the dictator's reputation based on a simple formula. """

        score = years_in_power + (wars_fought * 2) + (enemies_killed * 0.5)
        return '{:,}'.format(max(score, 0))
    
    @classmethod
    def amin(cls):
        return cls("Idi Amin", "Uganda", 8)
    

if __name__ == "__main__":

    Genghis = Dictator(name="Genghis Khan",
                       country="Mongolia",
                       years_in_power=21)
    
    print(Genghis.name)
    print(Genghis.calculate_reputation(years_in_power=Genghis.years_in_power,
                                       wars_fought=50,
                                       enemies_killed=100_000))
    
    Amin = Dictator.amin()
    print(Amin.name, Amin.country, Amin.years_in_power)
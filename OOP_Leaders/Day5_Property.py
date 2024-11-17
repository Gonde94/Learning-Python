"""
The @property decorator allows us to create a read-only property.
It is also used to give special functionality to certain methods to make them
act as getters, setters, or deleters when we define properties in a class.

We can define how a property is accessed, set and deleted by defining its
getter, setter, and deleter methods. These give extra "power" to it.

We can use a setter method to implement constraints on the property value.
"""


class Leader:
    """
    Creates a leader.
    """

    def __init__(self, name: str, country: str, year_of_birth: int, year_of_death: int):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth
        self.year_of_death = year_of_death

    @property
    def age(self) -> int:
        return self.year_of_death - self.year_of_birth
    

class General(Leader):
    """
    Creates a military leader.
    """

    def __init__(self, name: str, country:str, 
                 year_of_birth: int, year_of_death: int, army_size: int):
        super().__init__(name, country, year_of_birth, year_of_death)
        self.army_size = army_size

        self._skills = {
            'Charisma': 0,
            'Oratory': 0,
            'Military strategy': 0,
            'Courage': 0,
            'Ruthlessness': 0
        }

    @property
    def skills(self):
        return self._skills
    
    @skills.setter
    def skills(self, skill_and_score):
        try:
            skill, score = skill_and_score
        except ValueError:
            raise ValueError("Pass an iterable with two items: skill and score.")
        
        sufficient_score = self.sufficient_score(score)

        if sufficient_score:
            self._skills[skill] = True
        else:
            self._skills[skill] = False
            print(f"{skill} test score was not sufficient so cannot be the General.")

    @skills.deleter
    def skills(self):
        print("Careful - you're deleting this General's skill test score!")
        del self._skills

    @staticmethod
    def sufficient_score(score) -> bool:
        """ Given a score, determine if a test was passed.  """
        if score > 5:
            return True
        else:
            return False
    

if __name__ == "__main__":

    Nobunaga = Leader(name="Oda Nobunaga", 
                      country="Japan",
                      year_of_birth=1534,
                      year_of_death=1582)
    print(f"{Nobunaga.name} age:", Nobunaga.age)
    # prints 48

    # Try to set age
    #Nobunaga.age = 54 # Results in attribute error

    Sitting_Bull = General(name="Sitting Bull",
                           country="Dakota Territory",
                           army_size=3_000,
                           year_of_birth=1831,
                           year_of_death=1890)
    
    Sitting_Bull.skills = ("Charisma", 8) 
    Sitting_Bull.skills = ("Oratory", 8) 
    Sitting_Bull.skills = ("Military strategy", 7)   
    Sitting_Bull.skills = ("Courage", 9) 
    Sitting_Bull.skills = ("Ruthlessness", 5) 
    print(Sitting_Bull.skills)

    del Sitting_Bull.skills
    print(Sitting_Bull.skills) # An attribute error as skills have been deleted
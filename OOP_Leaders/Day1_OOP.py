class Leader:
    """
    Creates a leader.
    """

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def says(self, words):
        return f"{self.name} says {words}"


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


class Prophet(Leader):
    """
    Creates a religious leader.
    """

    def __init__(self, name, country, religion):
        super().__init__(name, country)
        self.religion = religion

        self._skills = {
            'Charisma': 0,
            'Empathy': 0,
            'Symbolism': 0,
            'Ritualistic knowledge': 0,
            'Philosophical knowledge': 0
        }


if __name__ == "__main__":

    Napoleon = Dictator(name="Napoleon",
                        country="France",
                        years_in_power=10)
    
    print("Name: ", Napoleon.name)
    print("Country: ", Napoleon.country)
    print("Years in power: ", Napoleon.years_in_power)
    print(Napoleon.says("Bonjour."))

    Jesus = Prophet(name="Jesus",
                    country="Judea",
                    religion="Judaism")
    
    print("Name: ", Jesus.name)
    print("Country: ", Jesus.country)
    print("Religion: ", Jesus.religion)
    print(Jesus.says("Hello, my child."))
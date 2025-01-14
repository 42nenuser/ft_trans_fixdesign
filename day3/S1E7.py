from S1E9 import Character


class Baratheon(Character):
    """
    Represents a Baratheon family member in the story.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Baratheon family member with a first name and a living state.
        
        :param first_name: The first name of the Baratheon family member.
        :param is_alive: Boolean indicating if the character is alive (default is True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        String representation of the Baratheon family member.
        """
        return f"{self.first_name} of the {self.family_name} family."

    def __repr__(self):
        """
        Formal string representation of the Baratheon family member.
        """
        return f"Baratheon('{self.first_name}', {self.is_alive})"

    def die(self):
        """
        Mark the Baratheon character as deceased by setting is_alive to False.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Represents a Lannister family member in the story.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Lannister family member with a first name and a living state.
        
        :param first_name: The first name of the Lannister family member.
        :param is_alive: Boolean indicating if the character is alive (default is True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        String representation of the Lannister family member.
        """
        return f"{self.first_name} of the {self.family_name} family."

    def __repr__(self):
        """
        Formal string representation of the Lannister family member.
        """
        return f"Lannister('{self.first_name}', {self.is_alive})"

    def die(self):
        """
        Mark the Lannister character as deceased by setting is_alive to False.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Class method to create a new Lannister family member.
        
        :param first_name: The first name of the Lannister family member.
        :param is_alive: Boolean indicating if the character is alive (default is True).
        :return: An instance of the Lannister class.
        """
        return cls(first_name, is_alive)

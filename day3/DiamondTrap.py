from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a King who has traits from both Baratheon and Lannister families.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a King with a first name and a living state.
        
        :param first_name: The first name of the King.
        :param is_alive: Boolean indicating if the King is alive (default is True).
        """
        super().__init__(first_name, is_alive)

    # Getter and Setter for 'eyes'
    def get_eyes(self) -> str:
        """
        Get the eye color of the King.
        :return: Eye color as a string.
        """
        return self.eyes

    def set_eyes(self, color: str):
        """
        Set the eye color of the King.
        :param color: The new eye color.
        """
        self.eyes = color

    # Getter and Setter for 'hairs'
    def get_hairs(self) -> str:
        """
        Get the hair color of the King.
        :return: Hair color as a string.
        """
        return self.hairs

    def set_hairs(self, color: str):
        """
        Set the hair color of the King.
        :param color: The new hair color.
        """
        self.hairs = color

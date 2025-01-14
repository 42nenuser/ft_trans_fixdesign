from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character in a story.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a first name and a living state.
        
        :param first_name: The first name of the character.
        :param is_alive: Boolean indicating if the character is alive (default is True).
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to mark the character as deceased.
        """
        pass


class Stark(Character):
    """
    Represents a Stark family member in the story.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Stark family member with a first name and a living state.
        
        :param first_name: The first name of the Stark family member.
        :param is_alive: Boolean indicating if the character is alive (default is True).
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Mark the Stark character as deceased by setting is_alive to False.
        """
        self.is_alive = False

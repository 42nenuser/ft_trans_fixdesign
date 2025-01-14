class Calculator:
    """
    A calculator class that performs scalar operations on a vector.
    """

    def __init__(self, vector: list[float]):
        """
        Initialize the Calculator with a vector.
        
        :param vector: A list of floats representing the vector.
        """
        self.vector = vector

    def __add__(self, scalar: float):
        """
        Add a scalar to each element of the vector.
        :param scalar: The scalar to add.
        :return: A new vector with the result.
        """
        return [x + scalar for x in self.vector]

    def __sub__(self, scalar: float):
        """
        Subtract a scalar from each element of the vector.
        :param scalar: The scalar to subtract.
        :return: A new vector with the result.
        """
        return [x - scalar for x in self.vector]

    def __mul__(self, scalar: float):
        """
        Multiply each element of the vector by a scalar.
        :param scalar: The scalar to multiply.
        :return: A new vector with the result.
        """
        return [x * scalar for x in self.vector]

    def __truediv__(self, scalar: float):
        """
        Divide each element of the vector by a scalar.
        :param scalar: The scalar to divide.
        :return: A new vector with the result.
        :raises ZeroDivisionError: If scalar is 0.
        """
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return [x / scalar for x in self.vector]

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Calculate the dot product of two vectors.
        
        :param V1: The first vector.
        :param V2: The second vector.
        :return: The dot product as a float.
        """
        return sum(x * y for x, y in zip(V1, V2))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Add two vectors element-wise.
        
        :param V1: The first vector.
        :param V2: The second vector.
        :return: A new vector with the result.
        """
        return [x + y for x, y in zip(V1, V2)]

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Subtract one vector from another element-wise.
        
        :param V1: The first vector.
        :param V2: The second vector.
        :return: A new vector with the result.
        """
        return [x - y for x, y in zip(V1, V2)]
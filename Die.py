import random


class Die:
    """
    This is the die class, which has an attribute value and a roll method for rolling the dice.
    value is a non public method, it has getters and setters for modifying it.
    """

    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def roll(self) -> int:
        """
        :return: a random integer between 1 and 6
        """
        self.value = random.randint(1, 6)
        return self.value




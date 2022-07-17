import random


class Die:
    def __init__(self) -> None:
        self._value = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def roll(self) -> int:
        self.value = random.randint(1, 6)
        return self.value




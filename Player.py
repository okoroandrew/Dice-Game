from Die import Die


class Player:
    def __init__(self, die: Die, name: str, is_human: bool) -> None:
        self._die = die
        self._is_human = is_human
        self._counter = 10
        self._name = name

    @property
    def is_human(self) -> bool:
        return self._is_human

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def die(self) -> Die:
        return self._die

    @property
    def name(self):
        return self._name

    def increment_counter(self) -> None:
        self._counter += 1

    def decrement_counter(self) -> None:
        self._counter -= 1

    def roll_the_die(self) -> int:
        return self._die.roll()





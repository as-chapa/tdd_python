from dataclasses import dataclass
from abc import ABCMeta
from bank import Bank

@dataclass
class Expression(metaclass=ABCMeta):
    def times(self, multiplier: int):
        pass
    def plus(self, addend):
        pass
    def reduce(self, bank: Bank, to: str):
        pass
from abc import ABCMeta
from bank import Bank

class Expression(metaclass=ABCMeta):
    def plus(self, addend):
        pass
    def reduce(self, bank: Bank, to: str):
        pass
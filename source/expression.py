from abc import ABCMeta

class Expression(metaclass=ABCMeta):
    def reduce(self, to: str):
        pass
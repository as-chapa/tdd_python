from dataclasses import dataclass
from expression import Expression
from sum import Sum
from bank import Bank

@dataclass
class Money(Expression):
    _amount : int
    _currency : str

    def __eq__(self, other):
        if not isinstance(other, Money): return False
        if not self._amount == other.amount: return False
        if not self._currency == other.currency: return False
        return True
    
    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def times(self,multiplier:int) -> Expression:
        return Money(self.amount * multiplier, self.currency)

    def plus(self,addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str):
        rate: int = Bank().rate(self.currency, to)
        return Money(self.amount / rate, to)

    @staticmethod
    def Dollar(amount: int):
        return Money(amount, 'USD')

    @staticmethod
    def Franc(amount: int):
        return Money(amount, 'CHF')

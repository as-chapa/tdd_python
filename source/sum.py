from dataclasses import dataclass
from expression import Expression
import money
from bank import Bank

@dataclass
class Sum(Expression):
    _augend: Expression
    _addend: Expression

    @property
    def augend(self):
        return self._augend

    @property
    def addend(self):
        return self._addend
    
    def reduce(self, bank: Bank, to: str):
        amount: int = self._augend.reduce(bank, to).amount + self._addend.reduce(bank, to).amount
        return money.Money(amount, to)

    def plus(self,addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self,multiplier:int) -> Expression:
        return Sum(self._augend.times(multiplier), self._addend.times(multiplier))

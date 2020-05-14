from expression import Expression
import money

class Sum(Expression):
    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend
    
    @property
    def augend(self):
        return self._augend

    @property
    def addend(self):
        return self._addend
    
    def reduce(self, to: str):
        amount: int = self._augend.amount + self._addend.amount
        return money.Money(amount, to)
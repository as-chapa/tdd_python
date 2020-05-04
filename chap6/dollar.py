import money

class Dollar(money.Money):
    def __init__(self,amount:int):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self,multiplier:int):
        return(Dollar(self.amount * multiplier))

    def equals(self,object) -> bool:
        dollar = object
        return self.amount == dollar.amount

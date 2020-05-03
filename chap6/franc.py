class Franc():
    __amount:int

    def __init__(self,amount:int):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self,multiplier:int):
        return(Franc(self.amount * multiplier))

    def equals(self,object) -> bool:
        franc = object
        return self.amount == franc.amount

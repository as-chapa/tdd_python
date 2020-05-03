class Dollar():
    __amount:int

    def __init__(self,amount:int):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def times(self,multiplier:int):
        return(Dollar(self.amount * multiplier))

    def equals(self,object) -> bool:
        dollar = object
        return self.amount == dollar.amount

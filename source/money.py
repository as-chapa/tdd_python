class Money():
    # pythonにはprotectedがないので、慣習的に「_」で定義する
    _amount : int
    _currency : str
    def __init__(self,amount:int, currency:str):
        self._amount = amount
        self._currency = currency

    # propetyデコレータで外部から直接変更しにくくする（言語特性上、禁止はできない）
    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def times(self,multiplier:int):
        return(Money(self.amount * multiplier, self.currency))

    def equals(self,object) -> bool:
        money:Money = object
        return self._amount == money.amount and self._currency == money.currency

    @staticmethod
    def Dollar(amount: int):
        return Dollar(amount, 'USD')

    @staticmethod
    def Franc(amount: int):
        return Franc(amount, 'CHF')

class Dollar(Money):
    pass

class Franc(Money):
    pass
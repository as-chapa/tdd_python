from abc import ABCMeta, abstractmethod

class Money(metaclass=ABCMeta):
    # pythonにはprotectedがないので、慣習的に「_」で定義する
    _amount : int
    _currency : str
    def __init__(self,amount:int, currency:str):
        self._amount = amount
        self._currency = currency

    # propetyデコレータで外部から直接変更しにくくする（言語特性上、禁止はできない）
    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @abstractmethod
    def times(self,multiplier:int):
        pass

    def equals(self,object) -> bool:
        money:Money = object
        return self._amount == money.amount and type(self) == type(money)

    @staticmethod
    def Dollar(amount: int):
        return Dollar(amount, 'USD')

    @staticmethod
    def Franc(amount: int):
        return Franc(amount, 'CHF')

class Dollar(Money):
    def times(self,multiplier:int) -> Money:
        return(Money.Dollar(self.amount * multiplier))

class Franc(Money):
    def times(self,multiplier:int) -> Money:
        return(Money.Franc(self.amount * multiplier))

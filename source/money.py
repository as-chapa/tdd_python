from expression import Expression
from sum import Sum
from bank import Bank

class Money(Expression):
    # pythonにはprotectedがないので、慣習的に「_」で定義する
    _amount : int
    _currency : str
    def __init__(self,amount:int, currency:str):
        self._amount = amount
        self._currency = currency
    
#    # unittestのassertEqualだとオブジェクトのIDの一致まで見るため、型＋値だけの比較を実装する
#    def __eq__(self, other):
#        if not isinstance(other, Money): return False
#        if not self._amount == other.amount: return False
#        if not self._currency == other.currency: return False

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
    
    def plus(self,addend) -> Expression:
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

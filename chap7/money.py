class Money():
    # pythonにはprotectedがないので、慣習的に「_」で定義する
    _amount : int
    def __init__(self,amount:int):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def equals(self,object) -> bool:
        money:Money = object
        return self.amount == money.amount

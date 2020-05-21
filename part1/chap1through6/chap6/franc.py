import money
class Franc(money.Money):
    def times(self,multiplier:int):
        return(Franc(self.amount * multiplier))

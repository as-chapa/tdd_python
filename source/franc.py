import money

class Franc(money.Money):
    def times(self,multiplier:int) -> money.Money:
        return(Franc(self.amount * multiplier))

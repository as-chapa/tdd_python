import money

class Dollar(money.Money):
    def times(self,multiplier:int) -> money.Money:
        return(Dollar(self.amount * multiplier))

import money

class Dollar(money.Money):
    def times(self,multiplier:int):
        return(Dollar(self.amount * multiplier))

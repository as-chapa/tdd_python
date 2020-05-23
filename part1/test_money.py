import unittest
# テストコードを別ディレクトリにする場合はここのimport指定を変える
from money import Money
from bank import Bank
from expression import Expression
from sum import Sum

class TestMoney(unittest.TestCase):
    # Arrange --
    five: Money = Money.Dollar(5)
    five_bucks: Expression = Money.Dollar(5)
    ten_flancs: Expression = Money.Franc(10)

    # Action & Assertion --
    def test_multiplication(self):
        self.assertEqual(Money.Dollar(10),self.five.times(2))
        self.assertEqual(Money.Dollar(15),self.five.times(3))
    
    def test_equality(self):
        self.assertEqual(Money.Dollar(5), Money.Dollar(5))
        self.assertNotEqual(Money.Dollar(5), Money.Dollar(6))
        self.assertNotEqual(Money.Franc(5), Money.Dollar(5))

    def test_currency(self):
        self.assertEqual('USD',Money.Dollar(1).currency)
        self.assertEqual('CHF',Money.Franc(1).currency)
    
    def test_simple_adddition(self):
        sum: Expression = self.five.plus(self.five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(sum,'USD')
        self.assertEqual(Money.Dollar(10), reduced)
    
    def test_plus_returns_sum(self):
        result: Expression = self.five.plus(self.five)
        sum: Sum = result
        self.assertEqual(self.five, sum.augend)
        self.assertEquals(self.five, sum.addend)

    def test_reduce_sum(self):
        sum: Expression = Sum(Money.Dollar(3), Money.Dollar(4))
        bank: Bank = Bank()
        result: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.Dollar(7).amount, result.amount)
    
    def test_reduce_money(self):
        bank: Bank = Bank()
        result: Money = bank.reduce(Money.Dollar(1),'USD')
        self.assertEqual(Money.Dollar(1), result)
    
    def test_recuce_money_different_currency(self):
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result: Money = bank.reduce(Money.Franc(2), "USD")
        self.assertEqual(Money.Dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate("USD","USD"))
    
    def test_mixed_addition(self):
        five_bucks: Expression = Money.Dollar(5)
        ten_flancs: Expression = Money.Franc(10)
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result: Money = bank.reduce(five_bucks.plus(ten_flancs), "USD")
        self.assertEqual(Money.Dollar(10), result)

    def test_sum_plus_money(self):
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum: Expression = Sum(self.five_bucks, self.ten_flancs).plus(self.five_bucks)
        result: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.Dollar(15), result)

    def test_sum_times(self):
        bank: Bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum: Expression = Sum(self.five_bucks, self.ten_flancs).times(2)
        result: Money = bank.reduce(sum, "USD")
        self.assertEqual(Money.Dollar(20), result)
    
    def test_sum_reduce(self):
        sum: Sum = Sum(self.five_bucks, self.ten_flancs)
        self.assertFalse(sum.reduce(self.five_bucks,"USD"))
    
if __name__ == '__main__':
    unittest.main()
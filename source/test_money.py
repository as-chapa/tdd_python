import unittest
# テストコードを別ディレクトリにする場合はここのimport指定を変える
from money import Money
from bank import Bank
from expression import Expression

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five: Money = Money.Dollar(5)
        self.assertEqual(Money.Dollar(10).amount,five.times(2).amount)
        self.assertEqual(Money.Dollar(15).amount,five.times(3).amount)
    
    def test_equality(self):
        self.assertTrue(Money.Dollar(5).equals(Money.Dollar(5)))
        self.assertFalse(Money.Dollar(5).equals(Money.Dollar(6)))
        self.assertFalse(Money.Franc(5).equals(Money.Dollar(5)))

    def test_currency(self):
        self.assertEqual('USD',Money.Dollar(1).currency)
        self.assertEqual('CHF',Money.Franc(1).currency)
    
    def test_simple_adddition(self):
        five: Money = Money.Dollar(5)
        sum: Expression = five.plus(five)
        bank: Bank = Bank()
        reduced: Money = bank.reduce(sum,'USD')
        self.assertEqual(Money.Dollar(10).amount, reduced.amount)

if __name__ == '__main__':
    unittest.main()
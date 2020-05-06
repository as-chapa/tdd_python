import unittest
# テストコードを別ディレクトリにする場合はここのimport指定を変える
from money import Money

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five: Money = Money.Dollar(5)
        # Pythonのインスタンスの等価性比較は、比較対象を明示しないといけないので、amountで比較
        # ただ、これって test_equality と同じことになっている気が。
        self.assertEqual(Money.Dollar(10).amount,five.times(2).amount)
        self.assertEqual(Money.Dollar(15).amount,five.times(3).amount)
    
    def test_equality(self):
        self.assertTrue(Money.Dollar(5).equals(Money.Dollar(5)))
        self.assertFalse(Money.Dollar(5).equals(Money.Dollar(6)))
        self.assertTrue(Money.Franc(5).equals(Money.Franc(5)))
        self.assertFalse(Money.Franc(5).equals(Money.Franc(6)))
        self.assertFalse(Money.Franc(5).equals(Money.Dollar(5)))

    def test_franc_multiplication(self):
        five = Money.Franc(5)
        # Pythonのインスタンスの等価性比較は、比較対象を明示しないといけないので、amountで比較
        # ただ、これって test_equality と同じことになっている気が。
        self.assertEqual(Money.Franc(10).amount,five.times(2).amount)
        self.assertEqual(Money.Franc(15).amount,five.times(3).amount)

if __name__ == '__main__':
    unittest.main()
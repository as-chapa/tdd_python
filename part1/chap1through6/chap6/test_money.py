import unittest
# テストコードを別ディレクトリにする場合はここのimport指定を変える
import dollar
import franc

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        # Pythonのインスタンスの等価性比較は、比較対象を明示しないといけないので、amountで比較
        # ただ、これって test_equality と同じことになっている気が。
        self.assertEqual(dollar.Dollar(10).amount,five.times(2).amount)
        self.assertEqual(dollar.Dollar(15).amount,five.times(3).amount)
    
    def test_equality(self):
        self.assertTrue(dollar.Dollar(5).equals(dollar.Dollar(5)))
        self.assertFalse(dollar.Dollar(5).equals(dollar.Dollar(6)))
        self.assertTrue(franc.Franc(5).equals(franc.Franc(5)))
        self.assertFalse(franc.Franc(5).equals(franc.Franc(6)))

    def test_franc_multiplication(self):
        five = franc.Franc(5)
        # Pythonのインスタンスの等価性比較は、比較対象を明示しないといけないので、amountで比較
        # ただ、これって test_equality と同じことになっている気が。
        self.assertEqual(franc.Franc(10).amount,five.times(2).amount)
        self.assertEqual(franc.Franc(15).amount,five.times(3).amount)

if __name__ == '__main__':
    unittest.main()
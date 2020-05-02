import unittest
# テストコードを別ディレクトリにする場合はここのimport指定を変える
import dollar

class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10,five.amount)

if __name__ == '__main__':
    unittest.main()
from fibonacci import fibonacci, fibonacci_1
from parameterized import parameterized, parameterized_class
import unittest

class TestContarPalabras(unittest.TestCase):
    @parameterized.expand([
        (1,1),
        (2,1),
        (3,2),
        (4,3),
        (5,5),
        (6,8)
    ])
    def test(self, number, result):
        self.assertEqual(fibonacci(number),result)

if __name__ == '__main__':
    unittest.main()
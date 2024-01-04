import unittest
from python_recap.fibonacci_sequence import fibonacci_sequence


class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_sequence(self):
        """
        Test that fibonacci_sequence returns the correct sequence
        """
        expected = {"result": [0, 1, 1, 2, 3], "sum": 7}
        actual = fibonacci_sequence(5)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

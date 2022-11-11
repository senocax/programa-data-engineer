import unittest
from functions.calculator import add
from functions.calculator import subtract
from functions.calculator import divide
from functions.calculator import multiply

class TestCalc(unittest.TestCase):

    def test_add(self):
        """Test add operation."""
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-3, -1), -4)

    def test_subtract(self):
        """Test subtract operation."""
        self.assertEqual(subtract(1, 5),-4)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-2, -2), 0)

    def test_multiply(self):
        """Test multiply operation."""
        self.assertEqual(multiply(10, 9), 90)
        self.assertEqual(multiply(-2, 2), -4)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        """Test divide operation."""
        self.assertEqual(divide(15, 5), 3)
        self.assertEqual(divide(-2, 1), -2)
        self.assertEqual(divide(5, 2), 2.5)

        with self.assertRaises(ZeroDivisionError):
            divide(25, 0)


if __name__ == '__main__':
    unittest.main()
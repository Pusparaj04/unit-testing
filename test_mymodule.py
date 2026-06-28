import unittest

from mypackage import square, double, add, multiply, divide

class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9)

    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3.1), -6.2)
        self.assertEqual(double(0), 0)

    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertEqual(add(2.3000, 4.3000), 6.6)
        self.assertNotEqual(add(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2.0, 3.0), 6.0)
        self.assertEqual(multiply(8, 0), 0)
        self.assertNotEqual(multiply(2, 0), 2)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(6.0, 3.0), 2.0)
        self.assertNotEqual(divide(8, 1), 1)
        self.assertEqual(divide(0, 10), 0)

unittest.main()
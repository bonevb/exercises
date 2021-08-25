from math import gcd


def lcm(one, two):
    return one.denominator * two.denominator // gcd(one.denominator, two.denominator)


class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError

    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return str(0)
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        if self.numerator == 0:
            return str(0)
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        return (self.numerator / self.denominator) == other

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)

        lcm1 = lcm(self, other)
        num1 = self.numerator * (lcm1 / self.denominator)
        num2 = other.numerator * (lcm1 / other.denominator)
        return Fraction(int(num1 + num2), lcm1)

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        if self.denominator == other.denominator and self.numerator - other.numerator != 0:
            return Fraction(self.numerator - other.numerator, self.denominator)

        lcm1 = lcm(self, other)
        num1 = self.numerator * (lcm1 / self.denominator)
        num2 = other.numerator * (lcm1 / other.denominator)
        fin_numerator = int(num1 - num2)
        return Fraction(int(num1 - num2), lcm1)

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        if self.numerator == 0:
            return 0
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        gcd1 = gcd(self.numerator, self.denominator)
        return Fraction(int(self.numerator / gcd1), int(self.denominator / gcd1))

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        if gcd(self.numerator, self.denominator) == 1 or self.numerator == 0:
            return True
        return False


from fractions import Fraction
import unittest


class FractionTests(unittest.TestCase):
    def test_create_fraction(self):
        a = Fraction(1, 2)
        num = 1
        denom = 2

        self.assertEqual(a.numerator, num)
        self.assertEqual(a.denominator, denom)

    def test_equal_fractions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 3)

        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_add_fractions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 3)
        d = a + b
        e = a + c

        self.assertEqual(d, Fraction(2,2))
        self.assertEqual(e, Fraction(5, 6))

    def test_sub_francions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 3)

        d = a - b
        e = a - c

        self.assertEqual(d.__repr__(), '0')
        self.assertEqual(e, Fraction(1, 6))

    def test_mul_fractions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        c = Fraction(1, 3)

        d = a * b
        e = a * c

        self.assertEqual(d, Fraction(1, 4))
        self.assertEqual(e, Fraction(1, 6))

    def test_simplify_fraction(self):
        a = Fraction(5, 2)
        b = Fraction(2, 2)
        c = Fraction(3, 6)

        self.assertEqual(a.simplify(), 5 / 2)
        self.assertEqual(b.simplify(), 1)
        self.assertEqual(c.simplify(), 1 / 2)

    def test_is_simplified_fractions(self):
        a = Fraction(5, 2)
        b = Fraction(2, 2)
        c = Fraction(3, 6)

        self.assertTrue(a.is_simplified(), True)
        self.assertFalse(b.is_simplified(), False)
        self.assertFalse(c.is_simplified(), False)


if __name__ == "__main__":
    unittest.main()

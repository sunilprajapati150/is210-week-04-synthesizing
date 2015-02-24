#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import decimal
import unittest
import task_01


class Task01TestCase(unittest.TestCase):
    """
    Test cases for Task 01.
    """

    def test_absolute_difference(self):
        """
        Tests the value of the ABSOLUTE_DIFFERENCE constant.
        """
        expected = decimal.Decimal('273.15')
        self.assertEqual(task_01.ABSOLUTE_DIFFERENCE, expected)

    def test_fahrenheit_to_celsius(self):
        """
        Tests that fahrenheit_to_celsius() returns correctly.
        """
        expected = ((decimal.Decimal('397') - 32) * 5) / 9
        returned = task_01.fahrenheit_to_celsius('397')
        self.assertEqual(returned, expected)

    def test_celsius_to_kelvin(self):
        """
        Tests that celsius_to_kelvin() returns correctly.
        """
        expected = decimal.Decimal(971) + decimal.Decimal('273.15')
        returned = task_01.celsius_to_kelvin(971)
        self.assertEqual(returned, expected)

    def test_fahrenheit_to_kelvin(self):
        """
        Tests that fahrenheit_to_kelvin() returns correctly.
        """
        expected = ((decimal.Decimal(228) - 32) * 5) / 9
        expected += decimal.Decimal('273.15')
        returned = task_01.fahrenheit_to_kelvin(228)
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import decimal
import unittest
import task_01


class Task02TestCase(unittest.TestCase):
    """
    Test cases for Task 02.
    """

    def test_absolute_difference(self):
        """
        Tests the value of the ABSOLUTE_DIFFERENCE constant.
        """
        expected = decimal.Decimal('273.15')
        self.assertEqual(task_01.ABSOLUTE_DIFFERENCE, expected)

    def test_celsius_to_kelvin(self):
        """
        Tests that celsius_to_kelvin() returns correctly.
        """
        expected = decimal.Decimal(971) + decimal.Decimal('273.15')
        returned = task_01.celsius_to_kelvin(971)
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()

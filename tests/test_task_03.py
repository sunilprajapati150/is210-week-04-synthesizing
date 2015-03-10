#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03."""


# Import Python libs
import decimal
import unittest
import task_01


class Task03TestCase(unittest.TestCase):
    """
    Test cases for Task 03.
    """

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

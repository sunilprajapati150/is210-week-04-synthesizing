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

    def test_fahrenheit_to_celsius(self):
        """
        Tests that fahrenheit_to_celsius() returns correctly.
        """
        expected = ((decimal.Decimal('397') - 32) * 5) / 9
        returned = task_01.fahrenheit_to_celsius('397')
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()

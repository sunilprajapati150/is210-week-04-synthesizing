#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A good docstring"""

ABSOLUTE_DIFFERENCE = int (273.15)
import decimal

def fahrenheit_to_celsius (degrees):
    round(degrees,2)
    f = ((degrees - 32.0)  * 5.0) / 9.0
    return 'Decimal(\'{0}\')'.format(f)

def celsius_to_kelvin(degrees):
    k = degrees + ABSOLUTE_DIFFERENCE
    return 'Decimal(\'{0}\')'.format(k)

def fahrenheit_to_kelvin(degrees):
    a = fahrenheit_to_celsius(degrees)
    b = celsius_to_kelvin(a)
    return 'Decimal(\'{0}\')'.format(b)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A good docstring"""

ABSOLUTE_DIFFERENCE = 273.15
import decimal

def fahrenheit_to_celsius (degrees):
    round(degrees,3)
    f = ((degrees - 32)  * 5) / 9
    print('Decimal(\'{0}\')'.format(f))
    
def celsius_to_kelvin(degrees):
    k = degrees + ABSOLUTE_DIFFERENCE
    print('Decimal(\'{0}\')'.format(k))

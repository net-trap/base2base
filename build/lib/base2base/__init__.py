# __init__.py

"""
base2base
~~~~~~~~~

A Python library that converts numbers from any base to any base, supporting bases 2 through 62.
"""

from .converter import convert, to_decimal, from_decimal

__all__ = ["convert", "to_decimal", "from_decimal"]
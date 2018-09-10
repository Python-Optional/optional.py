"""compatible_abc

This module exports a single class, CompatibleABC.
It is necessary to provide the same behavior in
Python 2 and Python 3.

The implementation was taken from https://stackoverflow.com/a/38668373
"""
from abc import ABCMeta


CompatibleABC = ABCMeta('ABC', (object,), {'__slots__': ()})

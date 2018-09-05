from abc import ABCMeta


CompatibleABC = ABCMeta('ABC', (object,), {'__slots__': ()})

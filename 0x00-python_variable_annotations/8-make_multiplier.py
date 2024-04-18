#!/usr/bin/env python3
"""module that has a function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """the function that returns a function
      that multiplies a float by a multiplier"""
    def func(num: float) -> float:
        """the function that multiplies a float by a multiplier"""
        nonlocal multiplier
        return (multiplier * num)
    return func

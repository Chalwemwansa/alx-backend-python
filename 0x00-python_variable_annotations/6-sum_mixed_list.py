#!/usr/bin/env python3
"""module contains a function that returns the sum from a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """the function that gets a mixed list of floats and ints
    then returns the sum as float"""
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return (sum)

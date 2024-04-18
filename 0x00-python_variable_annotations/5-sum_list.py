#!/usr/bin/env python3
"""module conatains a function called sum_list which sums up floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for num in input_list:
        sum += num
    return sum

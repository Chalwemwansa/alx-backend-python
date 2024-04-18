#!/usr/bin/env python3
"""module contains afunction that receives
    a string and an int or float then returns a tuple"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """the function that returns a tuple from a given number and string"""
    product: float = v ** 2
    return (k, product)

#!/usr/bin/env python3
"""module contains a function
    that returns a tuple from a sequence of numbers"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
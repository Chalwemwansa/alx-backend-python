#!/usr/bin/env python3
"""module contains a function that collects 10 random numbers
    from an async generator"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function that collects values from an async
        function and returns the list"""
    my_list = [i async for i in async_generator()]
    return my_list

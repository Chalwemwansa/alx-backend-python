#!/usr/bin/env python3
"""module contains a function that prints 10 random numbers
    and yields the value for a second"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """function that perfomrs the async operation"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

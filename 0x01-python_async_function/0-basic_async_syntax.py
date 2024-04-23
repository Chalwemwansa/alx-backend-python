#!/usr/bin/env python3
"""module contains an async function that shows
    how async functions work in python"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """the function that delays for a given number of seconds then prints
    the float of the number of seconds it waits before printing a value"""
    if max_delay > 0:
        rand = random.uniform(0, max_delay + 1)
    elif max_delay < 0:
        rand = random.uniform(0, max_delay - 1)
    else:
        rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return (rand)

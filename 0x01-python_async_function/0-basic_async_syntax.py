#!/usr/bin/env python3
"""module contains an async function that shows
    how async functions work in python"""
import asyncio
import random


async def wait_random(max_delay=10):
    """the function that delays for a given number of seconds then prints
    the float of the number of seconds it waits before printing a value"""
    rand = random.uniform(0, max_delay + 1)
    await asyncio.sleep(rand)
    return (rand)

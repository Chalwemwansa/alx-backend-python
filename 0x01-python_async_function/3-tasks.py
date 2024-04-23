#!/usr/bin/env python3
"""module contains a function task_wait_random that returns an syncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """function takes in max_delay and returns the asyncio task generated
        from wait_random"""
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task

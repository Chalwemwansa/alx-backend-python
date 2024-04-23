#!/usr/bin/env python3
"""module contains afunction that checkd the running time
    of the async function created previously"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """the async function that returns the runningtime
        from running multiple instances at the same time"""
    task1 = asyncio.create_task(async_comprehension())
    task2 = asyncio.create_task(async_comprehension())
    task3 = asyncio.create_task(async_comprehension())
    task4 = asyncio.create_task(async_comprehension())
    start_time = time.time()
    result = await asyncio.gather(task1, task2, task3, task4)
    elapsed_time = time.time() - start_time
    return elapsed_time

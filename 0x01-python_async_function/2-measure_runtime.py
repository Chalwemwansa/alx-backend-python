#!/usr/bin/env python3
"""module contains a function that measure the elapsed time for
    running an async function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """function that returns the total time elapsed, total_time / n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n

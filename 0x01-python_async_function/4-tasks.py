#!/usr/bin/env python3
"""module contains a function that runs multiple coroutines at the same time"""
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """function that takes in two integers and runs a given async function
        multiple times"""
    pending_tasks = [task_wait_random(max_delay) for i in range(n)]
    result = []

    while pending_tasks:
        tasks = await asyncio.wait(pending_tasks,
                                   return_when=asyncio.FIRST_COMPLETED)
        completed_task, pending_tasks = tasks
        for task in completed_task:
            result.append(task.result())
    return result

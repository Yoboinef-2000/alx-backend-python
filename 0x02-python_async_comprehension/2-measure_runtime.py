#!/usr/bin/env python3

"""Implementing asyncio gather."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measure the run time."""
    startTimerBaby = time.time()

    coroutines = []
    for _ in range(4):
        coroutines.append(async_comprehension())
    await asyncio.gather(*coroutines)

    endTimer_WellKinda = time.time()
    olympicTime = endTimer_WellKinda - startTimerBaby
    return olympicTime

#!/usr/bin/env python3

"""More async await"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time (n: int, max_delay: int) -> float:
    """Measure the time wait_n takes."""
    startTimerBaby = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTimer_WellKinda = time.time()

    olympicTime = endTimer_WellKinda - startTimerBaby 
    return olympicTime / n
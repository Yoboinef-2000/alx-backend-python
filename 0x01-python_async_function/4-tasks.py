#!/usr/bin/env python3

"""More async, await."""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async coroutines."""
    delayList: List[float] = []
    for _ in range(n):
        delulu = await task_wait_random(max_delay)
        delayList.append(delulu)
    return sorted(delayList)

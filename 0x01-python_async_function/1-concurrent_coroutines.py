#!/usr/bin/env python3

"""More async, await."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """Async coroutines."""
    delayList: List[float] = []
    for _ in range(n):
        delulu = await wait_random(max_delay)
        delayList.append(delulu)
    return sorted(delayList)
    

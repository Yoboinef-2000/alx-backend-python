#!/usr/bin/env python3

"""Async basics."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine."""
    theDelay = random.uniform(0, max_delay)
    await asyncio.sleep(theDelay)
    return theDelay

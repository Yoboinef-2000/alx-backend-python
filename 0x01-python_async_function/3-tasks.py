#!/usr/bin/env python3

"""More async exercises."""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio Task to execute wait_random."""
    coroKoroba: Coroutine = wait_random(max_delay)
    return asyncio.create_task(coroKoroba)

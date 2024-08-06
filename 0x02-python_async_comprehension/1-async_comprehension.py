#!/usr/bin/env python3

"""Async comprehension."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Tu comprehende?"""
    allNumbers: List[float] = []
    async for valueBeingIterated in async_generator():
        allNumbers.append(valueBeingIterated)
    return allNumbers

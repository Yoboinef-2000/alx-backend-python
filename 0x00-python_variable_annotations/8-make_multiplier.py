#!/usr/bin/env python3

"""Type annotated make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply'em up."""
    def laFunctioneMultiplier(x: float) -> float:
        return x * multiplier
    
    return laFunctioneMultiplier

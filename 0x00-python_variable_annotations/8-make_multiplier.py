#!/usr/bin/env python3
"""Type-annotated func make_multiplier that takes a float multiplier as arg"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Return product of multiplier and n."""
        return n * multiplier
    return multiply

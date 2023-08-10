#!/usr/bin/env python3
"""Async comprehension module."""


# import random
from typing import List
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    result = [i async for i in generator()]
    return result

#!/usr/bin/env python3
"""Async comprehension module."""


import asyncio
# import random
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    result = [i async for i in generator()]
    return result

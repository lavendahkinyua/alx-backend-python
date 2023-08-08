#!/usr/bin/env python3
"""use the code from wait_n and make it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""


import asyncio
from typing import List
wait_random = __import__('3-tasks.py').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of delays in ascending order."""
    temp = 0
    waiting = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))

    
    for i in range(0, len(waiting)):
        for j in range(i + 1, len(waiting)):
            if (waiting[i] > waiting[j]):
                temp = waiting[i]
                waiting[i] = waiting[j]
                waiting[j] = temp
    return waiting

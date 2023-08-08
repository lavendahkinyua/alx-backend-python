#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay.

wait_n returns the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
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

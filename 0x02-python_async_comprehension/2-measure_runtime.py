#!/usr/bin/env python3
'''Simple module since it has a simple funciton.'''
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure total time of running async function 4 times and return it.'''
    start_time = time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return time() - start_time

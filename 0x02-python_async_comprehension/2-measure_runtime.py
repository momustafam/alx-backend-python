#!/usr/bin/evn python3
'''Simple module since it has a simple funciton.'''
import asyncio
from time import time

comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure total time of running async function 4 times and return it.'''
    start_time = time()
    await asyncio.gather(comp(), comp(), comp(), comp())
    return time() - start_time

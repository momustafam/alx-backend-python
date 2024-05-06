#!/usr/bin/env bash
'''Simple module since it has a simple funciton.'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Return a wait_random task.'''
    return asyncio.create_task(wait_random(max_delay))

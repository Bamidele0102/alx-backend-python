#!/usr/bin/env python3
"""This measures the total execution-time(runtime) for wait_n(n, max_delay)"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[summary]

    Args:
        n (int, optional): [description]. Defaults to 0.
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description] - total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))

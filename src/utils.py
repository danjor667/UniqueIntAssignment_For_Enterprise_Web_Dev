"""
usefull custom functions and class for the program
"""
from typing import Iterable
from collections import defaultdict
from memory_profiler import profile, memory_usage


def read_file(file_path: str):
    seen = defaultdict(int)
    with open(file_path, "r") as file:
        for integer in file:
            integer = integer.rstrip('\n')
            try:
                integer = int(integer)
            except Exception:
                continue
            seen[integer] += 1
            if seen[integer] == 1:
                yield integer

@profile
def generator_sort(generator: Iterable[int]):
    yield from sorted(generator)
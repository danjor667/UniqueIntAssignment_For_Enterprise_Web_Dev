"""
usefull custom functions and class for the program
"""
from typing import Iterable

class CheckDouble():
    """
    class to check for duplicate
    entries in the file
    """
    def __init__(self):
        self.check = {}

    def add(self, element):
        """
        adding element and keeping track of its count
        :param element:
        """
        if element not in self.check:
            self.check[element] = 1
        else:
            self.check[element] += 1

    def get_value(self, element):
        """
        getting the current count of the element
        :param element:
        :return count of element:
        """
        return self.check.get(element)


def read_file(file_path: str):
    """
    reading the contenet of the file and generating
    on demand to reduce memory usage for storing it
    :param file_path:
    :return:
    """
    seen = CheckDouble()
    with open(file_path, "r") as file:
        for integer in file:
            integer = integer.rstrip('\n')
            try:
                integer = int(integer)
            except Exception:
                continue
            seen.add(integer)
            if seen.get_value(integer) == 1:
                yield integer


def generator_sort(generator: Iterable[int]):
    yield from sorted(generator)


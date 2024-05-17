"""
useful custom functions and class for the program
"""
from typing import Iterable


class CheckDouble:
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


def readAndProcessFile(file_path: str) -> Iterable[int]:
    """
    reading the content of the file and generating
    it on demand to reduce memory usage storing all the items
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


def selection_sort(arr: list[int], reverse=False) -> None:
    """
    custom sorting function
    implementing the selection sort algorithm
     to sort the array of integers
    """
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if not reverse:
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]


def writeFile(integers, output_file_path: str) -> None:
    with open(output_file_path, "w") as f:
        for integer in integers:
            f.write(str(integer)+"\n")

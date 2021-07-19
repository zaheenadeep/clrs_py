from random import randrange
from typing import List, Any


class Quicksort:
    @staticmethod
    def sort(arr: List[Any]):
        Quicksort._quicksort(arr, 0, len(arr) - 1)

    @staticmethod
    def _quicksort(arr: List[Any], p: int, r: int) -> None:
        if p < r:
            q = Quicksort._partition(arr, p, r)
            Quicksort._quicksort(arr, p, q - 1)
            Quicksort._quicksort(arr, q + 1, r)

    @staticmethod
    def _partition(arr: List[Any], p: int, r: int) -> int:
        x = arr[r]
        i = p - 1
        for j in range(p, r):
            if arr[j] <= x:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i + 1


class RandomizedQuicksort:
    @staticmethod
    def sort(arr: List[Any]):
        RandomizedQuicksort._quicksort(arr, 0, len(arr) - 1)

    @staticmethod
    def _quicksort(arr: List[Any], p: int, r: int) -> None:
        if p < r:
            q = RandomizedQuicksort._partition(arr, p, r)
            RandomizedQuicksort._quicksort(arr, p, q - 1)
            RandomizedQuicksort._quicksort(arr, q + 1, r)

    @staticmethod
    def _partition(arr: List[Any], p: int, r: int) -> int:
        i = randrange(p, r + 1)
        arr[i], arr[r] = arr[r], arr[i]
        return Quicksort._partition(arr, p, r)


if __name__ == '__main__':
    array = [6, 3, 567, 9, 3, 2, 46, 7, 3]
    RandomizedQuicksort.sort(array)
    print(array)

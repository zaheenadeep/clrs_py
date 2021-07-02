"""Solution to https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array """

from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        MaxHeap.heapsort(nums)
        return (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)


class MaxHeap:

    def __init__(self):
        self._data = []
        self._heap_size = 0

    def __len__(self):
        return self._heap_size

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    @classmethod
    def _left(cls, i):
        return 2 * i + 1

    @classmethod
    def _right(cls, i):
        return 2 * i + 2

    @classmethod
    def _parent(cls, i):
        return (i - 1) // 2

    def _max_heapify(self, i):
        data = self._data
        size = self._heap_size

        l = self._left(i)
        r = self._right(i)

        if l < size and data[l] > data[i]:
            largest = l
        else:
            largest = i
        if r < size and data[r] > data[largest]:
            largest = r

        self._swap(i, largest)

        if largest != i:
            self._max_heapify(largest)

    def build_max_heap(self, data):
        self._data = data
        self._heap_size = len(data)
        for i in range(self._heap_size // 2 - 1, -1, -1):
            self._max_heapify(i)

    @classmethod
    def heapsort(cls, data):
        max_heap = MaxHeap()
        max_heap.build_max_heap(data)
        for i in range(max_heap._heap_size - 1, max_heap._heap_size - 3, -1):
            max_heap._swap(0, i)
            max_heap._heap_size -= 1
            max_heap._max_heapify(0)


if __name__ == '__main__':
    nums = [3, 4, 5, 2]
    print(Solution().maxProduct(nums))

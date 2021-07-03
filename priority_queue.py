from math import inf
from max_heap import MaxHeap

class MaxPriorityQueue(MaxHeap):
    def __init__(self):
        MaxHeap.__init__(self)

    def maximum(self):
        return self._data[0]

    def extract_max(self):
        if self._heap_size < 1:
            raise HeapUnderflowError
        max, self._data[0] = self._data[0], self._data[self._heap_size-1]
        self._heap_size -= 1
        self._max_heapify(0)
        return max

    def increase_key(self, i, key):
        if key < self._data[i]:
            raise ValueError("key is smaller than the current key")
        while i > 0 and key > self._data[self._parent(i)]:
            self._data[i] = self._data[self._parent(i)]
            i = self._parent(i)
        self._data[i] = key

    def insert(self, key):
        self._heap_size += 1
        if self._heap_size > len(self._data) or len(self._data) == 0:
            self._data.append(-inf)
        else:
            self._data[self._heap_size - 1] = -inf

        self.increase_key(self._heap_size - 1, key)


class HeapUnderflowError(Exception):
    pass

if __name__ == '__main__':
    pq = MaxPriorityQueue()
    pq.insert(1).insert(16).insert(14).insert(10).insert(8).insert(7).insert(9).insert(3).insert(2).insert(4)

    print(pq)
    print(pq.extract_max())
    # print(pq.maximum())
    print(pq)
    print(len(pq))

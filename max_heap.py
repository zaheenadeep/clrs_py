class MaxHeap:

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def _swap(self, index1, index2):
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]

    def __init__(self):
        self._data = []
        self._heap_size = 0

    def _max_heapify(self, i):
        l = MaxHeap._left(i)
        r = MaxHeap._right(i)

        if l < self._heap_size and self._data[l] > self._data[i]:
            largest = l
        else:
            largest = i

        if r < self._heap_size and self._data[r] > self._data[largest]:
            largest = r

        if largest != i:
            self._swap(i, largest)
            self._max_heapify(largest)

    def build_max_heap(self, data):
        self._data = data
        self._heap_size = len(data)
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._max_heapify(i)

    @classmethod
    def heapsort(cls, data):
        max_heap = MaxHeap()
        max_heap.build_max_heap(data)
        for i in range(len(max_heap._data) - 1, 0, -1):
            max_heap._swap(i, 0)
            max_heap._heap_size -= 1
            max_heap._max_heapify(0)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return self._heap_size


if __name__ == "__main__":
    heap = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    MaxHeap.heapsort(heap)
    print(heap)
    print(len(heap))

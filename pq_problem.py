from typing import List


"""Solution to https://leetcode.com/problems/merge-k-sorted-lists/ """

from math import inf


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

class ModNode:
    def __init__(self, list_node, idx):
        self.node = list_node
        self.idx = idx

    def __lt__(self, other):
        if type(other) is float:
            return self.node.val < other
        else:
            return self.node.val < other.node.val

    def __gt__(self, other):
        if type(other) is float:
            return self.node.val > other
        else:
            return self.node.val > other.node.val

    def __eq__(self, other):
        if type(other) is float:
            return self.node.val == other
        else:
            return self.node.val == other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = MinPriorityQueue()
        for idx, head_node in enumerate(lists):
            if head_node is None:
                continue
            queue.insert(ModNode(head_node, idx))

        if len(queue) == 0:
            return None

        curr = queue.extract_min_ln()
        head = curr
        while len(queue) != 0:
            curr.next = queue.extract_min_ln()
            curr = curr.next

        return head


class MinHeap:

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

    def _min_heapify(self, i):
        l = MinHeap._left(i)
        r = MinHeap._right(i)

        if l < self._heap_size and self._data[l] < self._data[i]:
            smallest = l
        else:
            smallest = i

        if r < self._heap_size and self._data[r] < self._data[smallest]:
            smallest = r

        if smallest != i:
            self._swap(i, smallest)
            self._min_heapify(smallest)

    def build_min_heap(self, data):
        self._data = data
        self._heap_size = len(data)
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._min_heapify(i)

    @classmethod
    def heapsort(cls, data):
        min_heap = MinHeap()
        min_heap.build_min_heap(data)
        for i in range(len(min_heap._data) - 1, 0, -1):
            min_heap._swap(i, 0)
            min_heap._heap_size -= 1
            min_heap._min_heapify(0)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return self._heap_size


class MinPriorityQueue(MinHeap):
    def __init__(self):
        MinHeap.__init__(self)

    def __str__(self):
        return str(MinHeap)

    def minimum(self):
        return self._data[0]

    def extract_min(self):
        if self._heap_size < 1:
            raise HeapUnderflowError
        min, self._data[0] = self._data[0], self._data[self._heap_size - 1]
        self._heap_size -= 1
        self._min_heapify(0)
        return min

    def extract_min_ln(self):
        if self._heap_size < 1:
            raise HeapUnderflowError
        min = self._data[0]
        if min.node.next is None:
            min = self.extract_min().node
        else:
            min = min.node
            self._data[0].node = self._data[0].node.next
            self._min_heapify(0)
        return min

    def decrease_key(self, i, key):
        if key > self._data[i]:
            raise ValueError("key is bigger than the current key")
        while i > 0 and key < self._data[self._parent(i)]:
            self._data[i] = self._data[self._parent(i)]
            i = self._parent(i)
        self._data[i] = key

    def insert(self, key):
        self._heap_size += 1
        if self._heap_size > len(self._data) or len(self._data) == 0:
            self._data.append(inf)
        else:
            self._data[self._heap_size - 1] = inf

        self.decrease_key(self._heap_size - 1, key)


class HeapUnderflowError(Exception):
    pass


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(0)
    print(Solution().mergeKLists([a,b]))
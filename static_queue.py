class StaticQueue:

    def __init__(self, size) -> None:
        self.data = [None] * (size + 1)
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.tail + 1 == self.head or (self.head == 0 and self.tail == len(self.data) - 1)

    def enqueue(self, elem):
        if self.is_full():
            raise QueueOverflow

        self.data[self.tail] = elem
        if self.tail == len(self.data) - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflow

        ret_val = self.data[self.head]
        if self.head == len(self.data) - 1:
            self.head = 0
        else:
            self.head += 1
        return  ret_val

    def __str__(self):
        return str(self.data) + ", head : " + self.head.__str__() + ", tail: " + self.tail.__str__()

class QueueUnderflow(Exception):
    pass

class QueueOverflow(Exception):
    pass

if __name__ == '__main__':
    queue = StaticQueue(3)

    queue.enqueue(3)
    queue.enqueue(True)
    queue.enqueue(8)
    print(queue)

    try:
        queue.enqueue("blah")
    except QueueOverflow:
        print("Caught")

    print(queue.dequeue())
    print(queue)

    print(queue.dequeue())
    print(queue)

    print(queue.dequeue())
    print(queue)

    try:
        queue.dequeue()
    except QueueUnderflow:
        print("Caught")
class Stack:
    def __init__(self) -> None:
        self.data = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, elem):
        if len(self.data) == self.top + 1:
            self.data.append(elem)
        else:
            self.data[self.top] = elem
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflow
        self.top -= 1
        return self.data[self.top + 1]

    def __str__(self):
        return self.data[:self.top+1].__str__();

class StackUnderflow(Exception):
    pass

if __name__ == '__main__':
    stack = Stack()

    try:
        print(stack.pop())
    except StackUnderflow:
        print("Caught")

    stack.push(3)
    stack.push(True)
    stack.push(8)
    print(stack)
    print(stack.pop())
    print(stack)

    print(stack.pop())
    print(stack)

    print(stack.pop())
    print(stack)

    try:
        print(stack.pop())
    except StackUnderflow:
        print("Caught")
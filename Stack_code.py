class Stack:

    def __init__(self):
        # self.data = data
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

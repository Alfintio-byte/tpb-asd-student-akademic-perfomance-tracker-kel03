class Stack:

    def __init__(self):

        self.items = []

    def push(self, data):

        self.items.append(data)

    def pop(self):

        return self.items.pop()
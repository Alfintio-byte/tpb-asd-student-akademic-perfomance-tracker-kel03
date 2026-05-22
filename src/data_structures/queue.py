class Queue:

    def __init__(self):

        self.items = []

    # =========================
    # ENQUEUE
    # =========================

    def enqueue(self, item):

        self.items.append(item)

    # =========================
    # DEQUEUE
    # =========================

    def dequeue(self):

        if not self.is_empty():

            return self.items.pop(0)

        return None

    # =========================
    # IS EMPTY
    # =========================

    def is_empty(self):

        return len(self.items) == 0

    # =========================
    # TAMPILKAN QUEUE
    # =========================

    def display(self):

        print("Queue:", self.items)
from src.data_structures.queue import Queue

def test_queue():

    queue = Queue()

    queue.enqueue(10)

    assert queue.dequeue() == 10
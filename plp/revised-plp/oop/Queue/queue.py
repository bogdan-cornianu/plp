__author__ = 'bogdan.cornianu'


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "Queue is empty."


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
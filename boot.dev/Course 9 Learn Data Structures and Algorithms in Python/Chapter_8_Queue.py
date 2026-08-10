#lesson 2
class Queue:
    def __init__(self):
        self.items = []
        self.queue_size = 0

    def push(self, item):
        self.items.insert(0, item)
        self.queue_size += 1

    def pop(self):
        if self.queue_size > 0:
            output = self.items[-1]
            self.items = self.items[:-1]
            self.queue_size -= 1
            return output
        return None

    def peek(self):
        if self.queue_size > 0:
            return self.items[-1]
        return None

    def size(self):
        return self.queue_size

#lesson 6
from queue import Queue

def matchmake(queue, user):
    name, action = user
    if action == "join":
        queue.push(name)
    elif action == "leave":
        queue.search_and_remove(name)
    if queue.size() >= 4:
        return f'{queue.pop()} matched {queue.pop()}!'
    return "No match found"
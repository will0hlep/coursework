#lesson 1
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val

#lesson 3
def backoff_delays(base: int):
    delay = base
    while True:
        yield delay
        delay *= 2

#lesson 4
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
    
#lesson 5
from node import Node

class LinkedList:
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
    
#lesson 6
from node import Node

class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
    
#lesson 7
from node import Node

class LinkedList:
    def add_to_head(self, node):
        if self.head == None and self.tail == None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
        self.tail = node
        
    def __init__(self):
        self.head = None
        self.tail = None

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

#lesson 8
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

class LLQueue:
    def remove_from_head(self):
        if self.head == None:
            return None
        head_node = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        head_node.next = None
        return head_node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
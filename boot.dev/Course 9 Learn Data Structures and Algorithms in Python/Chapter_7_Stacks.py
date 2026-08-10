#lesson 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

#lesson 4
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def pop(self):
        if self.size() == 0:
            return None
        output = self.items[-1]
        self.items = self.items[:-1]
        return output

#lesson 7
from stack import Stack

def is_balanced(input_str):
    parentheses_stack = Stack()
    for i in input_str:
        if i == "(":
            parentheses_stack.push(i)
        elif i == ")":
            if parentheses_stack.pop() is None:
                return False
    return parentheses_stack.peek() == 0
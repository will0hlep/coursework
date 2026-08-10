#lesson 5
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None:
            self.val = val
        elif self.val > val:
            if self.left == None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif self.val < val:
            if self.right == None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
        return None
    
#lesson 7
class BSTNode:
    def get_min(self):
        if self.left == None:
            return self.val
        return self.left.get_min()

    def get_max(self):
        if self.right == None:
            return self.val
        return self.right.get_max()

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#lesson 8
class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        elif self.val > val and self.left is None:
            self.left = self.left.delete(val)
        elif self.val < val and self.right is None:
            self.right = self.right.delete(val)
        elif self.val == val
            if self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                successor = self.right
                while successor.left is not None:
                    successor = successor.left
                self.val = successor.val
                self.right = self.right.delete(self.val)
        return self

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
#lesson 11
class BSTNode:
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
            if self.left is not None:
                self.left.preorder(visited)
            if self.right is not None:
                self.right.preorder(visited)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#lesson 12
class BSTNode:
    def postorder(self, visited):
        if self.val is not None:
            if self.left is not None:
                self.left.postorder(visited)
            if self.right is not None:
                self.right.postorder(visited)
            visited.append(self.val)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#lesson 13
class BSTNode:
    def inorder(self, visited):
        if self.val is not None:
            if self.left is not None:
                self.left.inorder(visited)
            visited.append(self.val)
            if self.right is not None:
                self.right.inorder(visited)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#lesson 14
class BSTNode:
    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)
        if self.right is None:
            return False
        return self.right.exists(val)

        # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

#lesson 15
class BSTNode:
    def height(self):
        if self.val is None:
            return 0
        left_height = 0
        right_height = 0
        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()
        return 1 + max(left_height, right_height)

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
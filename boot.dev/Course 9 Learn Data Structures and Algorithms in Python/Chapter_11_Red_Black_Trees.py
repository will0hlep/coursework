#lesson 3
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil


    def insert(self, val):
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return
        new_node = RBNode(val)
        new_node.red = True
        new_node.parent = parent
        new_node.left = self.nil
        new_node.right = self.nil
        if parent is None:
            self.root = new_node
        elif parent.val < val:
            parent.right = new_node
        elif parent.val > val:
            parent.left = new_node
        return
    
#lesson 6
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent is not self.nil:
            if pivot_parent.right is not self.nil:
                pivot = pivot_parent.right
                pivot_parent.right = pivot.left
                if pivot.left is not self.nil:
                    pivot.left.parent = pivot_parent
                pivot.parent = pivot_parent.parent
                if self.root == pivot_parent:
                    self.root = pivot
                elif pivot_parent == pivot_parent.parent.left:
                    pivot_parent.parent.left = pivot
                elif pivot_parent == pivot_parent.parent.right:
                    pivot_parent.parent.right = pivot
                pivot.left = pivot_parent
                pivot_parent.parent = pivot
        return

    def rotate_right(self, pivot_parent):
        if pivot_parent is not self.nil:
            if pivot_parent.left is not self.nil:
                pivot = pivot_parent.left
                pivot_parent.left = pivot.right
                if pivot.right is not self.nil:
                    pivot.right.parent = pivot_parent
                pivot.parent = pivot_parent.parent
                if self.root == pivot_parent:
                    self.root = pivot
                elif pivot_parent == pivot_parent.parent.right:
                    pivot_parent.parent.right = pivot
                elif pivot_parent == pivot_parent.parent.left:
                    pivot_parent.parent.left = pivot
                pivot.right = pivot_parent
                pivot_parent.parent = pivot

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

#lesson 7
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)
    
    def fix_insert(self, new_node):
        current_node = new_node
        while current_node != self.root and current_node.parent.red == True:
            parent = current_node.parent
            grandparent = parent.parent
            if grandparent.right == parent:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent
                else:
                    if current_node == parent.left:
                        current_node = parent
                        self.rotate_right(current_node)
                        parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            elif grandparent.left == parent:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent
                else:
                    if current_node == parent.right:
                        current_node = parent
                        self.rotate_left(current_node)
                        parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False
            
    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
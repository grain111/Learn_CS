class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        nd = self.root
        while True:
            if value > nd.val:
                if nd.right == None:
                    nd.right = Node(value)
                    nd.right.parent = nd
                    break
                else:
                    nd = nd.right
            else:
                if nd.left == None:
                    nd.left = Node(value)
                    nd.left.parent = nd
                    break
                else:
                    nd = nd.left

    def find(self, key, root=0):
        root = root if root is not 0 else self.root
        if root == None:
            return None
        elif root.val == key:
            return root.val
        elif root.val > key:
            return self.find(key, root.left)
        else:
            return self.find(key, root.right)

    def next(self, node):
        if node.right:
            nd = node.right
            while nd.left != None:
                nd = nd.left
            return nd
        else:
            nd = node
            while nd.parent.val < node.val:
                if nd.parent.parent == None:
                    return None
                nd = nd.parent
            return nd.parent

    def sorted(self):
        lst = []
        smallest = self.root
        while smallest.left != None:
            smallest = smallest.left
        while smallest:
            lst.append(smallest.val)
            smallest = self.next(smallest)
        return lst

    # Add deletion, and self balancing


class Node(object):

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return "Node of value: {}".format(self.val)

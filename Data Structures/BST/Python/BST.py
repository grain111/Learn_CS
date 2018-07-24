from  collections import namedtuple
class BST(object):

    def __init__(self):
        self.root = None

    def __str__(self):
        height = self.root.height
        char_width = 3
        parameters = [None] * (height + 1)
        spacing = 1
        width = (2 ** height) * char_width + (2 ** height - 1) * spacing
        RowParam = namedtuple("row_parameters", ['padding', 'spacing'])

        for i in range(len(parameters) - 1, -1, -1):
            padding = 0 if i == height else (parameters[i + 1].spacing - char_width) // 2 + char_width + parameters[i + 1].padding
            space_between = (width - padding * 2 - 2 ** i * char_width)
            spacing = space_between if i == 0 else space_between // (2 ** i - 1)
            parameters[i] = RowParam(padding, spacing)

        for lvl in range(height + 1):
            if lvl == 0: nodes = [self.root]
            else:
                temp =  [None] * (2 ** lvl)
                for i, n in enumerate(nodes):
                    temp[2 * i] = n.left if n else None
                    temp[2 * i + 1] = n.right if n else None
                nodes = [node for node in temp]

            node_vals = [str(x.val).zfill(char_width) if x else (" " * char_width) for x in nodes]
            pad = parameters[lvl].padding
            print(" " * pad + (" " * parameters[lvl].spacing).join(node_vals) + " " * pad)

        return "{}".format(width)

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

        # Updating height of the nodes
        if (nd.right == None) ^ (nd.left == None):
            while nd != None:
                left_child_height = 0 if nd.left == None else nd.left.height
                right_child_height = 0 if nd.right == None else nd.right.height
                max_child_height = max(left_child_height, right_child_height)
                nd.height = max_child_height + 1
                nd = nd.parent

    def find(self, key, root=0):
        root = root if root is not 0 else self.root
        if root == None:
            return None
        elif root.val == key:
            return root
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

    def get_level(self, level, root=0):

        root = self.root if root == 0 else root

        if root == None:
            pass
        elif level == 0:
            yield root
        else:
            yield from self.get_level(level - 1, root.left)
            yield from self.get_level(level - 1, root.right)

    def sorted(self):
        lst = []
        smallest = self.root
        while smallest.left != None:
            smallest = smallest.left
        while smallest:
            lst.append(smallest.val)
            smallest = self.next(smallest)
        return lst

    def delete(self, node):
        if node.left == None and node.right == None:
            parent = node.parent
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

        elif (node.left == None) ^ (node.right == None):
            parent = node.parent
            child = node.left if node.left else node.right
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child

        else:
            minimum = node.right
            while minimum.left:
                minimum = minimum.left
            temp = node.val
            node.val = minimum.val
            minimum.val = temp
            self.delete(minimum)



class Node(object):

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return "Node of value: {}".format(self.val)

from BST import BST

class AVL(BST):

    def __init__(self):
        super().__init__()

    def insert(self, value):
        super().insert(value)
        nd = self.find(value)
        self.balance(nd)

    def delete(self, node):
        node_to_check = node.parent if node.parent else self.root
        super().delete(node)
        self.balance(node_to_check)

    def balance(self, node):
        while node != None:
            if self.get_diff(node) == -2:
                if self.get_diff(node.right) < 0:
                    self.LR(node)
                else:
                    self.RR(node.right)
                    self.LR(node)

            elif self.get_diff(node) == 2:
                if self.get_diff(node.left) > 0:
                    self.RR(node)
                else:
                    self.LR(node.left)
                    self.RR(node)

            node = node.parent

    def RR(self, node):
        y = node
        x = y.left

        A = x.left
        B = x.right
        C = y.right

        x.parent = y.parent
        if y.parent:
            if y.parent.right == y: y.parent.right = x
            elif y.parent.left == y: y.parent.left = x
        else:
            self.root = x

        x.right = y
        y.parent = x

        y.left = B
        if B: B.parent = y

        self.update_heights(y)

    def LR(self, node):
        x = node
        y = x.right

        A = x.left
        B = y.left
        C = y.right

        y.parent = x.parent
        if x.parent:
            if x.parent.right == x: x.parent.right = y
            elif x.parent.left == x: x.parent.left = y
        else:
            self.root = y

        y.left = x
        x.parent = y

        x.right = B
        if B: B.parent = x

        self.update_heights(x)

    def get_diff(self, node):
        l_height = node.left.height if node.left else -1
        r_height = node.right.height if node.right else -1
        return l_height - r_height

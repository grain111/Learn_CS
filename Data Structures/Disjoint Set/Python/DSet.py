class DSet(object):
    """Disjoint sets implemetation with union by rank."""

    def __str__(self):
        return str([[x.parent.data, x.data] for x in self.sets])
    def __init__(self):
        self.sets = []

    def make_set(self, val):
        self.sets.append(Node(val))

    def find(self, val):
        for n in self.sets:
            if n.data == val:
                node = n
        try:
            stack = []
            while node.parent != node:
                stack.append(node)
                node = node.parent
            for n in stack:
                n.parent = node
            return node
        except UnboundLocalError:
            print("There is no such element in sets!")

    def union(self, a, b):
        set_a = self.find(a)
        set_b = self.find(b)

        if set_a.rank >= set_b.rank:
            set_b.parent = set_a
            set_a.rank += 1
        else:
            set_a.parent = set_b
            set_b.rank += 1

class Node(object):
    def __init__(self, val):
        self.data = val
        self.rank = 0
        self.parent = self

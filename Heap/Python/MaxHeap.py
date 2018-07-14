class max_heap(object):
    def __init__(self):
        self.heap = []

    def __str__(self):
        return list(self.heap)

    def swap(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
        # print("swapped {} with {}".format(self.heap[a], self.heap[b]))

    def get_parent(self, index):
        return (index - 1) // 2

    def get_child(self, index, val):
        """left child: val = 1, right child: val = 2"""
        ind = (index) * 2 + val
        return ind if ind < len(self.heap) else None

    def insert(self, num):
        self.heap.append(num)
        index = len(self.heap) - 1
        while self.heap[index] > self.heap[self.get_parent(index)] and index != 0:
            self.swap(index, self.get_parent(index))
            index = self.get_parent(index)

    def extract(self):
        if len(self.heap) == 0: return None
        self.swap(0, len(self.heap) - 1)
        ans = self.heap.pop()
        index = 0
        while (self.get_child(index, 1) != None and self.get_child(index, 2) != None):
            children = []
            if self.get_child(index, 1): children.append(self.get_child(index, 1))
            if self.get_child(index, 2): children.append(self.get_child(index, 2))
            max_child = max(children, key = lambda x: self.heap[x])
            if self.heap[max_child] > self.heap[index]:
                self.swap(max_child, index)
                index = max_child
            else: break
        return ans

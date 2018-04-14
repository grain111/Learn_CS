class Node(object):

    def __init__(self, val):
        self.val = val
        self.pointer = None


class SLL(object):

    def __init__(self):
        self.head = None

    def push_front(self, key):
        new_node = Node(key)
        if self.head:
            new_node.pointer = self.head
            self.head = new_node
        else:
            self.head = new_node

    def pop_front(self):
        if self.head and self.head.pointer:
            value = self.head.val
            self.head = self.head.pointer
            return value
        else:
            self.head = None
            return None

    def push_back(self, key):
        new_node = Node(key)
        nd = self.head
        if self.head:
            while nd.pointer:
                nd = nd.pointer
            nd.pointer = new_node
        else:
            self.head = new_node

    def pop_back(self):
        nd = self.head
        if self.head and self.head.pointer:
            while nd.pointer.pointer:
                nd = nd.pointer
            value = nd.pointer.val
            nd.pointer = None
            return value
        else:
            self.head = None
            return None

    def empty(self):
        if not self.head:
            return True
        else:
            return False

    def get(self, index):
        counter = 0
        nd = self.head
        while nd:
            if counter == index:
                return nd.val
            counter += 1
            nd = nd.pointer

    def front(self):
        return self.head.val

    def back(self):
        nd = self.head
        if self.head and self.head.pointer:
            while nd.pointer.pointer:
                nd = nd.pointer
            return nd.pointer.val
        else:
            return None

    def insert(self, index, key):
        if index == 0:
            self.push_front(key)
        else:
            new_node = Node(key)
            nd = self.head
            counter = 0
            while nd:
                if counter == index - 1:
                    new_node.pointer = nd.pointer
                    nd.pointer = new_node
                    break
                else: nd = nd.pointer
                counter += 1

    def erase(self, index):
        if index == 0:
            self.pop_front()
        else:
            nd = self.head
            counter = 0
            while nd:
                if counter == index - 1:
                    nd.pointer = nd.pointer.pointer
                    break
                else: nd = nd.pointer
                counter += 1

    def nth_val_from_end(self, index):
        return self.get(len(self) - index - 1)

    def __len__(self):
        count = 0
        nd = self.head
        while nd:
            count += 1
            nd = nd.pointer
        return count

    def __str__(self):
        list = []
        nd = self.head
        while nd:
            list.append(nd.val)
            nd = nd.pointer
        return str(list)

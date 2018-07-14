class hash_table(object):
    def __init__(self, m=20):
        self.m = m
        self.table = [None]*m

    def hash_simple(self, n):
        return n

    def get_index(self, hash_func, n):
        return hash_func(n) % self.m

    def insert(self, num):
        index = self.get_index(self.hash_simple, num)
        if self.table[index]:
            self.table[index].append(num)
        else:
            self.table[index] = [num]

    def get(self, num):
        index = self.get_index(self.hash_simple, num)
        if self.table[index] != None:
            for val in self.table[index]:
                if val == num:
                    return num
        return None

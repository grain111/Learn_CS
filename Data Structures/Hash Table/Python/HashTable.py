class hash_table(object):
    def __init__(self, m=20):
        self.m = m
        self.table = [None]*m

    def hash_simple(self, n):
        return n

    def hash_int(self, n):
        a = 34
        b = 2
        p = 982451653
        return (a * n + b) % p

    def hash_str(self, str):
        x = 31
        p = 982451653
        hash = 0
        for i in range(len(str) - 1, 0, -1):
            hash = (hash * x + ord(str[i])) % p
        return hash

    def get_index(self, n):
        if type(n) == str:
            n = self.hash_str(n)
        return self.hash_int(n) % self.m

    def insert(self, key, val):
        index = self.get_index(key)
        if self.table[index]:
            self.table[index].append([key, val])
        else:
            self.table[index] = [[key, val]]

    def get(self, key):
        index = self.get_index(key)
        if self.table[index] != None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise ValueError("Key not found!")

    def set(self, key, new_val):
        index = self.get_index(key)
        if self.table[index] != None:
            for i, ent in enumerate(self.table[index]):
                if ent[0] == key:
                    self.table[index][i][1] = new_val
                    return
        raise ValueError("Key not found!")

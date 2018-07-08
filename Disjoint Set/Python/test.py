from DSet import DSet

my_set = DSet()
my_set.make_set(5)
my_set.make_set(1)
my_set.make_set(34)
my_set.make_set(38)
my_set.make_set(39)

my_set.union(39, 5)
my_set.union(38, 5)
my_set.union(1, 34)
my_set.union(34, 5)

my_set.find(34)

print(my_set)

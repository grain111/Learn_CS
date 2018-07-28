from AVL import AVL
from BST import BST

bin = AVL()

# RR
# bin.insert(5)
# bin.insert(7)
# bin.insert(4)
# bin.insert(8)
# bin.insert(10)

# LL

# bin.insert(8)
# bin.insert(9)
# bin.insert(3)
# bin.insert(2)
# bin.insert(1)

# double on right

# bin.insert(8)
# bin.insert(7)
# bin.insert(20)
# bin.insert(25)
# bin.insert(21)

# double on left

arr = [10,8,25,20,30,22,23]
for i in arr: bin.insert(i)
bin.delete(bin.find(30))
print(bin)

import time, random

from KSuba import simple_mul, kar_mul


arg = []
for j in range(10**1):
    a = random.randint(0, 10**70)
    b = random.randint(0, 10**70)
    arg.append([a, b])

start = time.time()
for arr in arg: simple_mul(arr[0], arr[1])
end = time.time()
print("Simple multipilcation: {}".format(end-start))

start = time.time()
for arr in arg: kar_mul(arr[0], arr[1])
end = time.time()
print("Kartsuba multipilcation: {}".format(end-start))

start = time.time()
for arr in arg: x = arr[0] * arr[1]
end = time.time()
print("Python multipilcation: {}".format(end-start))

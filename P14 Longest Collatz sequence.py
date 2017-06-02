import time, re

start = time.time()

sample = []

testlen = 0

j = 0
for i in range(500000,1000001):
    sample.append(i)
    j = i
    while j != 1:
        if j % 2 == 0:
            j /= 2
        else:
            j = 3*j + 1
        sample.append(j)
    if len(sample) > testlen:
        testlen = len(sample)
        print("Longest chain is created by number {0}".format(i))
    sample = []


elapsed = time.time() - start


print("Result returned in {0:.5f} seconds".format(elapsed))

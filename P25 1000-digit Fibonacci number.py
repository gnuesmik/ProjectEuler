import time

start = time.time()

flist = [1, 1]

one = 1
two = 1
num = 1

for i in range(1,100000):
    num = one + two
    flist.append(num)
    two = one
    one = num

for x in flist:
    if len(str(x)) >= 1000:
        print(flist.index(x) + 1)
        print(x)
        print(len(str(x)))
        break

elapsed = time.time() - start


print("Result returned in {0:.5f} seconds".format(elapsed))

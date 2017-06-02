import itertools, math, time, random

start = time.time()


sqlist = []
for i in itertools.count():
    sqlist.append(i**2)
    if len(sqlist) > 1000:
        break

del sqlist[0]

for x in sqlist:
    for y in sqlist:
        for z in sqlist:
            if x + y == z:
                x = math.sqrt(x)
                y = math.sqrt(y)
                z = math.sqrt(z)
                if x + y + z == 1000:
                    print("{0}^2 + {1}^2 = {2}^2 \n {0} + {1} + {2} = 1000 also! \n {0} * {1} * {2} = {3}".format(x, y, z, x*y*z))
                    break


elapsed = time.time() - start

print("Result returned in {0:.5f} seconds".format(elapsed))

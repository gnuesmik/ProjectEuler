import time, math

start = time.time()

sum = 0
for x in str(math.factorial(100)):
    sum += int(x)

print(sum)


elapsed = time.time() - start


print("Result returned in {0:.5f} seconds".format(elapsed))

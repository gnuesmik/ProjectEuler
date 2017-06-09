import time, re

start = time.time()

num = 2 ** 1000
nums = str(num)
sum = 0
print(nums)
for n in nums:
    sum += int(n)
print(sum)

elapsed = time.time() - start


print("Result returned in {0:.5f} seconds".format(elapsed))

import itertools, time

start = time.time()

primelist = []

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for x in itertools.count():
    if isPrime(x) == True:
        primelist.append(x)
    elif x > 2000000:
        break

del primelist[0:2]

sum = 0
for n in primelist:
    sum += n

print(sum)


elapsed = time.time() - start

print("result returned in %s seconds" % (elapsed))

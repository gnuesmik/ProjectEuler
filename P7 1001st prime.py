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
    elif len(primelist) == 10005:
        break

del primelist[0:2]
print(primelist[10001])


elapsed = time.time() - start

print("result returned in %s seconds" % (elapsed))
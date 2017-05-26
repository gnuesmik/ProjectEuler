import time, itertools

start = time.time()

primelist = []
bn = 0

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for x in itertools.count():
    if isPrime(x) == True:
        primelist.append(x)
    elif len(primelist) == 100000:
        break

del primelist[0:2]
print(len(primelist))

for x in primelist:
    if 600851475143 % x == 0:
        bg = x


print(bg)



elapsed = time.time() - start

print("result returned in %s seconds" % (elapsed))

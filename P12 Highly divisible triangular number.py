import itertools, time

start = time.time()

facdic = dict()
def factors(n):
    for m in range(1, n+1):
        if n % m == 0:
            if n not in facdic:
                facdic[n] = []
                facdic[n].append(m)

            else:
                facdic[n].append(m)



trilist = []

store = 0
new = 0

for x in itertools.count():
    if not x > 500000:
        store += x
        trilist.append(store)
    else:
        break

del trilist[0]

print(len(trilist))

print(trilist.index(76576500))

for y in trilist[12370:]:
    factors(y)
    if len(facdic[y]) < 499:
        print("Insufficient factors for trianguler number %d. Factor number is only %d" % (y, len(facdic[y])))
        del facdic[y]
    elif len(facdic[y]) >= 500:
        print(y)
        print(len(facdic[y]))
        break


elapsed = time.time() - start

print("result returned in %s seconds" % (elapsed))

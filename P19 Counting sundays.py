import time, re

start = time.time()


week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days = 0
count = 1
sunday = 0
firstday = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
firstdayl = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

for x in range(1901, 2001):
    if x % 4 == 0 and x % 100 != 0:
        days = 366
    elif x % 100 == 0 and x % 400 == 0:
        days = 366
    else:
        days = 365

    for y in range(1, days + 1):
        if count == 7:
            count = 0
        elif count == 6:
            if days == 365 and y in firstday:
                sunday += 1
            elif days == 366 and y in firstdayl:
                sunday += 1
        count += 1
print("First day of the month during the 20th century, there are {0} Sundays".format(sunday))







elapsed = time.time() - start


print("Result returned in {0:.5f} seconds".format(elapsed))

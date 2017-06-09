import time, re

start = time.time()

data = {
0: "",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety",
}

sum = 0
number = ""
hundred = ""
ten = ""
one = ""
store = ""

for n in range(1,1000):
    number = str(n)
    if n >= 100:
        hundred = int(number[0])
        ten = int(number[1])
        one = int(number[2])
        if n % 100 == 0:
            sum += len(data[hundred]) + 7

            print(data[hundred] + "hundred")

        else:
            sum += len(data[hundred]) + 10

            print(data[hundred] + "hundredand",end="")

            if ten == 1:
                ten = int(number[1:])
                sum += len(data[ten])

                print(data[ten])

            else:
                ten *= 10
                sum += len(data[ten]) + len(data[one])

                print(data[ten] + data[one])

    elif n >= 10:
        ten = int(number[0])
        one = int(number[1])
        if ten == 1:
            ten = int(number)
            sum += len(data[ten])

            print(data[ten])

        else:
            ten *= 10
            sum += len(data[ten]) + len(data[one])

            print(data[ten] + data[one])

    else:
        one = int(number)
        sum += len(data[one])

        print(data[one])

sum = sum + 11
print(sum)

elapsed = time.time() - start
print("Result returned in {0:.5f} seconds".format(elapsed))

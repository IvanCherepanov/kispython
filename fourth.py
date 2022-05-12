import math


def main(n):
    if n == 0:
        return -0.12
    elif n >= 1:
        return main(n - 1) - 63 * (math.cos(1 - (main(n - 1)) ** 3 / 81 - (main(n - 1)) ** 2)) ** 2
    return 0


def main2(n):
    res = []
    res.append(-0.12)
    for i in range(1, n + 1):
        temp = res[i - 1]
        res.append(temp - 63 * (math.cos(1 - temp ** 3 / 81 - temp ** 2)) ** 2)
    return res[n]

print(main(2)==main2(2))
print(main(8)==main2(8))
print(main(2))
print(main(8))
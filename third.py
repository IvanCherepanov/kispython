import math


def main(n, a, m):
    res1 = 0
    res2 = 0
    for i in range (1, a + 1):
        for c in range (1, n + 1):
            temp = (c ** 3 + (i/8)) ** 7
            temp2 = temp/46
            res1 += temp2

    for c in range (1, m + 1):
        for k in range (1, a + 1):
            temp = 80 * math.atan(k)- c ** 5
            res2 += temp

    return  (res1 + res2)
    

print(main(8, 2, 4))
print(main(6, 8, 6))
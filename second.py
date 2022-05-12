import math


def main(x):
    if x < 123:
        return 1+13*x**2
    elif x >= 123 and x < 143:
        return x ** 4 / 35
    elif x >= 143 and x < 236:
        return 70 * x ** 3 - math.exp(x)
    elif x >= 236:
        t = 70 * (x + 1 + 35 * x**2)**5
        return t + (x ** 2 + 34 * x ** 3) ** 3


print(main(148))

print(main(50))
print(main(205))
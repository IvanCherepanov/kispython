def maskA(number, begin, end):
    begin = 0
    end = 14
    number = number >> begin #сдвиг к началу


def main(x):
    temp_var = int(bin(x)[2:],2)

    a = temp_var & 0b11111111111111
    temp_var = temp_var >> 14

    b = temp_var & 0b11111111111111
    temp_var = temp_var >> 14

    c = temp_var & 0b1
    temp_var = temp_var >> 1

    d = temp_var

    d = d<<29
    b = b<<15
    a = a<<1
    return d|b|a|c



print(main(0x951facb4), 0x8a3f5969)
print(main(0x790bc3a5), 0x7217874b)

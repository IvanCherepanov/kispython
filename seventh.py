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

"""
a
'0b111'
1001 & bin(7)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    1001 & bin(7)
TypeError: unsupported operand type(s) for &: 'int' and 'str'
 1001 & (bin(7))

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    1001 & (bin(7))
TypeError: unsupported operand type(s) for &: 'int' and 'str'
int(0xb85b554d)
3092993357
bin(0xb85b554d)
'0b10111000010110110101010101001101'
0b10111000010110110101010101001101>>2
773248339
bin(0b10111000010110110101010101001101>>2)
'0b101110000101101101010101010011'
bin(0b10111000010110110101010101001101>>3)
bin(0b10111000010110110101010101001101&bin(15))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bin(0b10111000010110110101010101001101&bin(15))
TypeError: unsupported operand type(s) for &: 'int' and 'str'
(0b10111000010110110101010101001101&bin(15))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (0b10111000010110110101010101001101&bin(15))
TypeError: unsupported operand type(s) for &: 'int' and 'str'
(0b10111000010110110101010101001101&0b1111)
13
"""
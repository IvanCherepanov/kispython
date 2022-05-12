part_zero = [1976, 1964]
part_one = ['XS', 'SWIFT']
part_two = [1999, 1961]
part_third = ['VHDL', 'CIRRU', 'JULIA']
def f(x):
    if x[2] == 1999:
        if x[1] == 'XS':
            if x[0] == 1976:
                return 0
            return 1
        if x[0] == 1976:
            return 2
        return 3
    if x[1] == 'XS':
        if x[3] == 'VHDL':
            return 4
        elif x[3] == 'CIRRU':
            return 5
        return 6
    if x[3] == 'VHDL':
        return 7
    elif x[3] == 'CIRRU':
        return 8
    return 9



print(f([1976, 'SWIFT', 1961, 'VHDL']), 7)
print(f([1964, 'XS', 1961, 'JULIA']), 6)
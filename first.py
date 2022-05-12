import math


def main(z,y):
    x = (26*((50*z**3)**4)-76*(math.sqrt(y))**5)/(y**4+60*z**2)
    t = 50*(math.log(8*y**3+1+78*z,2))**4
    k = (math.log(z))**3
    return  ("%.2e" % (x+t+k))
    

print(main(0.93, 0.12))
print(main(0.08, 0.09))


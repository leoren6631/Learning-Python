import math

def quadratic(a, b, c):
    if a != 0:
        x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
        return (x1, x2)
    else:
        return('wrong input')

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(0,2,3))
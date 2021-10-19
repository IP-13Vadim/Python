# 19. Задані дійсні числа x, y. Визначити, чи належить точка з координатами (x, y)
# заштрихованій частині площини.
from math import fabs

r = 3
x = float(input("Enter x coordinate:"))
y = float(input("Enter y coordinate:"))

result1 = "The point belongs to the shaded part of the plane"
result2 = "The point does not belongs to the shaded part of the plane"

if (x ** 2) + (y ** 2) >= (r ** 2) and fabs(x) < 3 and fabs(y) < 3 and x>0:
    print(result1)
elif x < 0 and y > 0:
    print(result2)


# 19. Задані дійсні числа x, y. Визначити, чи належить точка з координатами (x, y)
# заштрихованій частині площини.

r = 3
x = float(input("Значення x:"))
y = float(input("Значення y:"))
if (x ** 2) + (y ** 2) >= (r ** 2) and abs(x) <= 3 and abs(y) <= 3:
    print("The point does not belongs to the shaded part of the plane")
elif x < 0 and y > 0:
    print("The point does not belongs to the shaded part of the plane")

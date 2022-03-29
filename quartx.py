import math
#ax2 + bx + c = 0
#D = b2 - 4ac
#D < 0 = нет корней
#D > 0 x1,x2 = -b +- sqrt(D)/2a
#D = 0 x = -b/2a
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
discr = ((b)**2) - (4*(a)*(c)) #D
if discr < 0:
    print("Корней нет")
elif discr == 0:
    x = (-b)/(2*(a))
    print(f"Корень уравнения: {x}")
else:
    x1 = (-b) + (math.sqrt(discr))
    x2 = (-b) - (math.sqrt(discr))
    print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
#хехе а я уже делал такое =)
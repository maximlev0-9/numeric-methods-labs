import math

integral = 0
m = 100
a = 1
b = 2
n = 2*m

h = (b-a)/n

def F(x:float):
    return -1*math.sqrt((9-x**2)**3)/3

def f(x:float):
    return x*math.sqrt(9-x**2)

fa = f(a)
fb = f(b)

for i in range(m):
    x = a+(2*i - 1)*h
    integral = integral + 4*f(x)
for i in range(m-1):
    x = a + 2*i*h
    integral = integral + 2*f(x)

integral = (h/3)*(fa+fb+integral)


print("counted integral: ", integral)

exact_integral = F(b) -F(a)

print("exact integral: ", exact_integral)

print("exact integral - counted: ", integral - exact_integral)

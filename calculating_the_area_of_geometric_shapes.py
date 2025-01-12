n = input()
pi = 3.14
if n == "треугольник":
    a, b, c = float(input()), float(input()), float(input())
    P = a + b + c
    p = P / 2
    print((p*(p - a)*(p - b)*(p - c)) ** 0.5)
elif n == "прямоугольник":
    a, b = float(input()), float(input())
    print(a * b)
elif n == "круг":
    r = float(input())
    print((r**2) * pi)
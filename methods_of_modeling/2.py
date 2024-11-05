def f(x):
    a = x ** 2 + 3 * x - 5
    return a

def derivative(x0, eps, g):
    Q = 10000
    h = 5
    n = 1
    while Q > eps:
        proizvodnaya = (g(x0 + h) - g(x0)) / h
        proizvodnaya2 = (g(x0 + 2 * h) - g(x0)) / (2 * h)
        Q = abs((proizvodnaya - proizvodnaya2) / (2 ** n - 1))
        h = h / 2
    return proizvodnaya

def main():
    x0 = int(input('Введите точку (x0): '))
    eps = float(input('Допустимая погрешность (eps): '))
    dx = derivative(x0, eps, f)
    print('Ответ: ', dx)


if __name__ == "__main__":
    main()

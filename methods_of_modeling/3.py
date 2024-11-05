#!/usr/bin/env python3
from math import *

def func(x, function_str):
    return eval(function_str)


def integrate_trapezoid(func, a, b, n, function_str):
    h = (b - a) / n
    sum = 0.5 * (func(a, function_str) + func(b, function_str))
    for i in range(1, n):
        sum += func(a + i * h, function_str)
    return h * sum


def main():    
    # Ввод данных пользователем
    function_str = input("Введите функцию (например, x**2 + sqrt(x)): ")
    lower_bound = float(input("Введите нижнюю границу интегрирования: "))
    upper_bound = float(input("Введите верхнюю границу интегрирования: "))
    n = 10
    # Вычисление интеграла
    result = integrate_trapezoid(func, lower_bound, upper_bound, n, function_str)
    if result is not None:
        print(
            f"Приближенное значение интеграла от {function_str} от {lower_bound} до {upper_bound} (шагов: {n}): {result:.4f}")


if __name__ == "__main__":
    main()


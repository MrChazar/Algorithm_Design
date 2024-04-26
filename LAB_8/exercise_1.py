"""
Zadanie nr 1 – mnożenie wielomianów
Zaimplementuj naiwną procedurę mnożenia wielomianów reprezentowanych przez współczynniki.
Wejście: dwie listy współczynników wielomianu.
Wyjście: lista współczynników wielomianu.
"""

a_x = [1, 0, 0, -2]
b_x = [0, -1, 3, 0]


def polynomial_multiplication(a, b):
    n = len(a)
    m = len(b)
    result = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += a[i] * b[j]
    return result


print(polynomial_multiplication(a_x, b_x))


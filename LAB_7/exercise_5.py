"""
Zadanie nr 4 – probabilistyczne testy piewszości
Zaimplementuj dwa algorytmy testowania pierwszości liczb
• test Fermata,
• test Millera-Rabina.
Wykorzystaj szybki algorytm potęgowania modulo.
Wejście: liczba potencjalnie pierwsza p.
Wyjście: rezultat testu pierwszości ww. algorytmami
"""
import random



def fermat_test(n, k):
    if pow(n, k - 1) % k != 1:
            return False
    return True


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

print(fermat_test(2, 88035))
print(miller_rabin_test(2, 88035))




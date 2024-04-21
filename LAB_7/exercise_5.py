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


def miller_rabin_test(a, p):
    yield

print(fermat_test(2, 88035))




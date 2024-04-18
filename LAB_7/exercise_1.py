"""
Zadanie nr 1 – rozkład na czynniki pierwsze
Zaimplementuj funkcję, która zwróci listę czynników pierwszych zadanej liczby naturalnej n. Zrób to rekurencyjnie,
sprawdzając podzielność liczby przez kolejne liczby naturalne (aż do ⌊√n⌋) –
rekurencja pojawia się, gdy liczba jest podzielna – wtedy uruchamiamy algorytm na jej dzielnikach.
Wejście: liczba naturalna n.
Wyjście: lista dzielników liczby n
"""
import math
# przechodzimy po podzielnikach od jakieś liczby aż do następnej chyba


def prime_factors(n, i=1):
    factors = []
    if (i <= n**1/2):
        if (n % i == 0):
            factors.append(i)
        factors += prime_factors(n, i + 1)
    return factors


if __name__ == '__main__':
    n = 363
    print(prime_factors(n, 1))
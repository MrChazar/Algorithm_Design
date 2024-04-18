"""
Zadanie nr 3 – największy wspólny dzielnik
3.1 Wyszukiwanie
Zaimplementuj funkcję szukającą największego wspólnego dzielnika dwóch liczb. Zrób to na dwa sposoby.
• Z wykorzystaniem rozkładu na czynniki pierwsze RNWD(a, b).
• Z wykorzystaniem algorytmu Euklidesa ENWD(a, b).
Wejście: dwie liczby a, b.
Wyjście: NW D(a, b) uzyskane na dwa sposoby
"""
import exercise_1 as ex1

def enwd(a, b):
    if b == 0:
        return a
    else:
        return enwd(b, a % b)


def rnwd(a, b):
    factors_a = ex1.prime_factors(a)
    factors_b = ex1.prime_factors(b)

    gcd = 1
    i = 0
    j = 0

    while i < len(factors_a) and j < len(factors_b):
        if factors_a[i] == factors_b[j]:
            gcd *= factors_a[i]
            i += 1
            j += 1
        elif factors_a[i] < factors_b[j]:
            i += 1
        else:
            j += 1

    return gcd


if __name__ == '__main__':
    a = 6
    b = 84
    print(f"ENWD: {enwd(a, b)}")
    print(f"RNWD: {rnwd(a,b)}")

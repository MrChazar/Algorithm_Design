"""
Zadanie nr 2 – sito Eratostenesa
Zaimplementuj sito Eratostenesa, aby wyznaczyć zbiór liczb pierwszych nie większych od zadanego p.
"""
import exercise_1 as ex1
import math
import numpy as np


def sieve_of_eratosthenes(p):
    x = np.linspace(1, 1, p)
    for n in range(2, int(p**1/2), 1):
        if x[n] == 1:
            for j in range(2, int(p/n), 1):
                x[n*j] = 0
    return x


if __name__ == '__main__':
    n = 363
    a = sieve_of_eratosthenes(n)

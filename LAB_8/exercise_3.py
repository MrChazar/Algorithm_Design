"""
Zadanie nr 3 – szybkie mnożenie wielomianów
Zaimplementuj szybką procedurę mnożenia wielomianów reprezentowanych przez współczynniki (wykorzystaj FFT)
Porównaj z naiwnym mnożeniem z zadania nr 1.
Wejście: dwie listy współczynników wielomianu.
Wyjście: lista współczynników wielomianu
"""
import scipy as scp
import numpy as np
import matplotlib.pyplot as plt
import exercise_1 as ex1


def fft_multiply_poly(poly1, poly2):
    m = len(poly1)
    n = len(poly2)
    total_degree = m + n - 1

    fft_size = 1 << (total_degree - 1).bit_length()

    fft_poly1 = np.fft.fft(poly1, fft_size)
    fft_poly2 = np.fft.fft(poly2, fft_size)

    fft_product = fft_poly1 * fft_poly2

    result = np.fft.ifft(fft_product).real

    return np.rint(result).astype(int)[:total_degree]

# Przykładowe współczynniki wielomianów
poly1 = [1, 2, 3]
poly2 = [4, 5, 6]

# Wykonaj mnożenie wielomianów
result_fft_multiply = fft_multiply_poly(poly1, poly2)
result_multiply = ex1.polynomial_multiplication(poly1, poly2)
print("Wynik Mnożenia FFT:", result_fft_multiply)
print("Wynik Mnożenia:", result_multiply)
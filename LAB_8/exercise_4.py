"""
4 Zadanie nr 4 – zestawienie
Eksperymentalnie zbadaj szybkość obu procedur mnożenia dla rosnącego stopnia wielomianu. Wyniki przedstaw na wykresach czasu działania algorytmów od rozmiaru wielomianu.
Wynik: wykresy czasu działania obu algorytmów od rozmiaru wielomianu
"""
import numpy as np
import timeit
import matplotlib.pyplot as plt


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


def polynomial_multiplication(a, b):
    n = len(a)
    m = len(b)
    result = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += a[i] * b[j]
    return result


def measure_time(algorithm, poly1, poly2):
    start_time = timeit.timeit()
    algorithm(poly1, poly2)
    end_time = timeit.timeit()
    return end_time - start_time


# Rozmiary wielomianów do przetestowania
sizes = [2 ** i for i in range(1, 20)]

# Czasy wykonania dla obu algorytmów
fft_times = []
naive_times = []

for size in sizes:
    # Generowanie losowych współczynników wielomianów
    poly1 = np.random.randint(1, 10, size)
    poly2 = np.random.randint(1, 10, size)

    # Pomiar czasu dla FFT
    fft_time = measure_time(fft_multiply_poly, poly1, poly2)
    fft_times.append(fft_time)

    # Pomiar czasu dla naiwnego algorytmu
    naive_time = measure_time(polynomial_multiplication, poly1, poly2)
    naive_times.append(naive_time)


# Wykres zależności czasu od rozmiaru wielomianu
plt.figure(figsize=(10, 6))
plt.plot(sizes, fft_times, label='FFT')
plt.plot(sizes, naive_times, label='Naiwne mnożenie')
plt.title('Zależność czasu od rozmiaru wielomianu')
plt.xlabel('Rozmiar wielomianu')
plt.ylabel('Czas [s]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()



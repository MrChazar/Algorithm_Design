"""
Zadanie nr 2 – FFT
Zaimplementuj szybki algorytm wyznaczania dyskretnej transformaty Fouriera (FFT).
Wejście: lista próbek sygnału.
Wyjście: lista harmonicznych.
"""
import scipy as scp
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 10)

signal = np.sin(t)

euler = 2.71828



def fft(a):
    n = len(a)

    if n == 1:
        return a

    wn = np.exp(-2j * np.pi / n)
    w = 1

    y_even = fft(a[::2])
    y_odd = fft(a[1::2])

    y = [0] * n
    for k in range(n // 2):
        y[k] = y_even[k] + w * y_odd[k]
        y[k + n // 2] = y_even[k] - w * y_odd[k]
        w *= wn
    return y



# Przykładowe użycie
a = [1, 2, 3, 4]
result = fft(a)
print("FFT wynik:", result)

t = np.linspace(0, 1, 100)
S = np.sin(np.pi*t)


# Obliczanie FFT przy użyciu Twojej funkcji
fft_result = fft(S.tolist())  # konwersja na listę, ponieważ funkcja oczekuje listy

plt.plot(t, S, label='Sinus')
plt.plot(t, np.abs(fft_result), label='Fouriera')

plt.legend()
plt.show()
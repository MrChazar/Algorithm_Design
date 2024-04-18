"""
Zadanie 3.2
Testy wydajności
Przygotuj procedurę testową do sprawdzenia czasu działania obu algorytmów.
Uruchamiaj RNWD(n, q) i ENWD(n, q) dla zadanej liczby n i dla kolejnych liczb naturalnych q do pewnego
zadanego m. Czasy działania obu algorytmów wyświetl na jednym wykresie.
Wejście: dwie liczby n, m.
Wyjście: wykres czasu działania dwóch algorytmów.
"""
import exercise_3 as ex3
import timeit
import matplotlib.pyplot as plt

n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
q_values = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

time_r = []
time_e = []

for n,q in zip(n_values, q_values):
    time_r.append(timeit.timeit(lambda: ex3.rnwd(n, q), number=1))
    time_e.append(timeit.timeit(lambda: ex3.enwd(n, q), number=1))


plt.plot(n_values, time_r, label='Algorytm RNWD')
plt.plot(n_values, time_e, label='Algorytm ENWD')
plt.xlabel('Rozmiar danych wejściowych')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania algorytmów nwd w zależności od implementacji')
plt.legend()
plt.grid(True)
plt.show()
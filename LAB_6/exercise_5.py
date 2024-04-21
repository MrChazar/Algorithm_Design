"""
Zadanie nr 5
Wyświetl wykresy czasu działania programów z zadań nr 2 i 3 w zależności od rozmiaru wejścia.
Dane wejściowe (listy liczb) generuj losowo.
Wyjście: wykresy czasu działania.
"""
import functions as func
import exercise_2 as ex2
import exercise_3 as ex3
import timeit
import matplotlib.pyplot as plt


n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280 , 290, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 850, 900]

time_be = []
time_sbe = []
time_me = []
time_ms = []

for n in n_values:
    input_data = func.fill_list(n)
    time_be.append(timeit.timeit(lambda: ex2.biggest_element(input_data, len(input_data)), number=1))
    time_sbe.append(timeit.timeit(lambda: ex2.second_biggest_element(input_data, len(input_data)), number=1))
    time_me.append(timeit.timeit(lambda: ex2.mean_element(input_data, len(input_data)), number=1))
    time_ms.append(timeit.timeit(lambda: ex3.merge_sort(input_data), number=1))

plt.plot(n_values, time_be, label='biggest_element')
plt.plot(n_values, time_sbe, label='second_biggest_element')
plt.plot(n_values, time_me, label='mean_element')
plt.plot(n_values, time_ms, label='merge_sort')
plt.xlabel('Rozmiar danych wejściowych')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania różnych algorytmów w zależności od rozmiaru danych')
plt.legend()
plt.grid(True)
plt.show()


"""
1 Zadanie nr 1 – przygotowanie danych
Dalsze zadania na liście są wykonywane z wykorzystaniem struktury opisującej flotę robotów mobilnych.
1. Pojedynczy robot jest krotką o polach (parametrach):
(a) TYP – tekst ze zbioru {„AGV”, „AFV”, „ASV”, „AUV” },
(b) CENA – liczba rzeczywista z przedziału [0, 10000] (PLN),
(c) ZASIĘG – liczba całkowita z przedziału [0, 100] (km),
(d) KAMERA – wartość binarna {0, 1} (jest, nie ma).
2. Przygotuj procedurę do generacji listy N robotów o losowo zadanych parametrach.
3. Wyświetl listę robotów i ich parametry (w tabelce: jeden robot – jeden wiersz).
4. Zaimplementuj funkcję zapisującą/odczytującą strukturę do/z pliku.
Wejście: długość listy N.
Wyjście: lista robotów wyświetlona na ekranie i zapisana do pliku.
"""

import numpy as np
import random
import pandas as pd

single_robot = ("AGV", 0, 0, 0, )

def generate_robots(n):
    robots = []

    for a in range(n):
        params = []

        t = random.randint(0,3)
        type = ""
        if (t == 0):
            type = "AGV"
        elif (t == 1):
            type = "AFV"
        elif (t == 2):
            type = "ASV"
        elif (t == 3):
            type = "AUV"

        price = random.uniform(0, 1000)

        ranged = random.randint(0, 100)

        camera = random.random()

        robots.append((type, price, ranged, camera))
    return robots


def show_robots(robots):
    df = pd.DataFrame(robots, columns =['Type', 'Price', 'Range', 'Camera'])
    print(df)


def write_robots(robots):
    df = pd.DataFrame(robots, columns=['Type', 'Price', 'Range', 'Camera'])
    df.to_csv("file.csv", index=False)
    print("Zapisano")


def read_robots():
    df = pd.read_csv("file.csv")

    types = df['Type']
    prices = df['Price']
    ranges = df['Range']
    cameras = df['Camera']

    robots = []
    for a,b,c,d in zip(types, prices, ranges, cameras):
        robots.append((a, b, c, d))

    return robots


def add_robot(robot):
    return (robot)


if __name__ == "__main__":
    robots = generate_robots(10)

    show_robots(robots)

    write_robots(robots)

    robots = read_robots()

    show_robots(robots)


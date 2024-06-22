# Zadanie 1:

import numpy as np
import random
import pandas as pd

# imie wiek kierunek ocena
single_student = ["Imie", 22, "informatyka", 4.5]


def generate_students(n):
    students = [('Jakub', 22, "statystyka", 5)]

    for a in range(n):

        t = random.randint(0,3)
        name = ""
        if (t == 0):
            name = "Jan"
        elif (t == 1):
            name = "Anna"
        elif (t == 2):
            name = "Piotr"
        elif (t == 3):
            name = "Adam"

        age = int(random.uniform(19, 30))

        d = random.randint(0, 3)
        course = ""
        if (d == 0):
            course = "informatyka"
        elif (d == 1):
            course = "statystyka"
        elif (d == 2):
            course = "wf"
        elif (d == 3):
            course = "inne"

        grade = random.randint(0, 5)


        students.append((name, age, course, grade))
    return students


def show_students(students):
    df = pd.DataFrame(students, columns =['Imie', 'Wiek', 'Kurs', 'Ocena'])
    print(df)


def write_students(students):
    df = pd.DataFrame(students, columns=['Imie', 'Wiek', 'Kurs', 'Ocena'])
    df.to_csv("students.csv", index=False)
    print("Zapisano")


def read_students():
    df = pd.read_csv("students.csv")

    names = df['Imie']
    ages = df['Wiek']
    courses = df['Kurs']
    grades = df['Ocena']

    students = []
    for a,b,c,d in zip(names, ages, courses, grades):
        students.append((a, b, c, d))
    return students


if __name__ == "__main__":

    n = int(input("Podaj N:"))
    print("Generowanie Studentów")
    students = generate_students(n)

    print("pokazywanie studentów")
    show_students(students)

    print("zapisywanie studentów")
    write_students(students)

    print("wczytywanie studentów")
    students = read_students()

    print("pokazywanie studentów")
    show_students(students)

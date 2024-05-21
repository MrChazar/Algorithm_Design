"""
Zadanie nr 1 – wyszukiwanie liniowe
Zaimplementuj algorytm wyszukiwania robota na liście.
Wyszukiwanie odbywa się względem listy dopuszczalnych wartości parametrów robota, tzn. dla każdego
parametru robota (TYP, CENA, ZASIĘG, KAMERA) zadana jest pojedyncza poszukiwana wartość, albo lista
dopuszczalnych wartości, albo None (wartość dowolna). Algorytm zwraca parametry pierwszego znalezionego
robota lub „brak”, jeśli robota nie znajdzie.
Np. [„AGV”, None, [5, 6, 7, 8, 9, 10], 1] odpowiada wyszukiwaniu robota typu „AVG”, o dowolnej cenie, o
zasięgu z przedziału 5 do 10, z kamerą.
Wejście: lista robotów (wczytywana z pliku), lista parametrów szukanego robota.
Wyjście: lista parametrów znalezionego robota lub „brak”.
Uwaga: realizując zadanie zaadoptuj (być może wielokrotnie) algorytm wyszukiwania liniowego.
"""

import LAB_9.exercise_1 as rob


def remove_robot(robots, removed_robots):
    removed = robots.pop(0)
    removed_robots.append(removed)
    print(f"Robot o parametrach: {removed} usunięty")


def clear_robots(robots, removed_robots):
    while robots != []:
        a = robots.pop(0)
        removed_robots.append(a)
    print("Roboty usunięte razem z tymi z oczyszczenia")
    rob.show_robots(removed_robots)


def search_robot(parameter, value_a, value_b):
    dict = {'Type': 0, 'Price': 1, 'Range': 2, 'Camera': 3}

    if value_b == "":
        if parameter == 'Type':
            result = [x for x in stack if x[dict[parameter]] == value_a]
            return result[0]
        else:
            result = [x for x in stack if float(x[dict[parameter]])]
            return result[0]
    else:
        result = [x for x in stack if float(x[dict[parameter]]) >= float(value_a) and float(x[dict[parameter]]) <= float(value_b)]
        return result[0]


stack = []
removed_stack = []

control = 'e'

while(control != 'q'):
    control = input(
        "Możesz - dodać robota : a, usunąć robota: r, wczytać roboty: l, wyświetlić roboty: p, wyszukać robota: f , wyjść: q "
        "Wybór:")


    if control == 'a':
        robot = rob.generate_robots(1)
        print(robot)
        stack.append(rob.add_robot(robot[0]))

    if control == 'r':
        remove_robot(stack, removed_stack)

    if control == 'c':
        clear_robots(stack, removed_stack)

    if control == 's':
        rob.write_robots(stack)

    if control == 'p':
        rob.show_robots(stack)

    if control == 'l':
        stack += rob.read_robots()

    if control == 'f':
        parameter = input("Wybierz parametr: 'Type', 'Price', 'Range', 'Camera':")
        value_a = input("Pierwsza wartość:")
        value_b = input("Druga wartość:")
        print("Wynik:")
        print(search_robot(parameter, value_a, value_b))
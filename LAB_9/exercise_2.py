"""
2 Zadanie nr 2
Zaimplementuj stos do przechowywania informacji o robotach.
Zaimplementuj algorytmy
• dodawania robota do stosu (parametry robota zadaje użytkownik),
• usuwania robota ze stosu i wyświetlenia jego parametrów,
• wyczyszczenia stosu i wyświetlenia parametrów wszystkich usuniętych robotów.
Wejście: pusty stos robotów.
Wyjście: stos robotów z dodanymi/usuniętymi robotami.
"""
import exercise_1 as rob


def remove_robot(robots, removed_robots):
    removed = robots.pop()
    removed_robots.append(removed)
    print(f"Robot o parametrach: {removed} usunięty")


def clear_robots(robots, removed_robots):
    while robots != []:
        a = robots.pop()
        removed_robots.append(a)
    print("Roboty usunięte razem z tymi z oczyszczenia")
    rob.show_robots(removed_robots)



stack = []
removed_stack = []

control = 'e'

while(control != 'q'):
    print("Aktualny Stan robotów")
    rob.show_robots(stack)

    print("Aktualnie usunięte roobty")
    rob.show_robots(removed_stack)

    control = input("Możesz dodać robota opcja: a, usunąć robota: r, wyczyścić stack: c, wyjść: q\n"
                    "Wybór:")


    if control == 'a':
        robot = rob.generate_robots(1)
        print(robot)
        stack.append(rob.add_robot(robot[0]))

    if control == 'r':
        remove_robot(stack, removed_stack)

    if control == 'c':
        clear_robots(stack, removed_stack)






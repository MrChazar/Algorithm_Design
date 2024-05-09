"""
4 Zadanie nr 4
Zaimplementuj listę z dowiązaniami do reprezentacji floty robotów. Zaproponuj postać klucza. Do przechowywania listy zastosuj reprezentację tablicową.
Zaimplementuj algorytmy
• dodawania elementu do listy,
• usuwania elementu z listy,
• wyszukiwania elementu na liście (i wyświetlania jego parametrów).
Wejście: pusta lista z dowiązaniami.
Wyjście: lista z dodanymi/usuniętymi robotami.
"""

import random
import pandas as pd


class Robot:
    def __init__(self, robot_id, type, price, ranged, camera):
        self.robot_id = robot_id
        self.type = type
        self.price = price
        self.ranged = ranged
        self.camera = camera
        self.next_robot = None


class RobotFleet:
    def __init__(self):
        self.head = None

    def add_robot(self, robot):
        if not isinstance(robot, Robot):
            raise ValueError("Invalid robot object")

        if self.head is None:
            self.head = robot
        else:
            current = self.head
            while current.next_robot is not None:
                current = current.next_robot
            current.next_robot = robot

    def remove_robot(self, robot_id):
        current = self.head

        if current is None:
            print("Robot fleet is empty")
            return

        # Check if the robot to remove is the head
        if current.robot_id == robot_id:
            self.head = current.next_robot
            return

        # Search for the robot by its ID
        prev = None
        while current is not None:
            if current.robot_id == robot_id:
                prev.next_robot = current.next_robot
                return
            prev = current
            current = current.next_robot

        print("Robot not found")

    def find_robot(self, robot_id):
        current = self.head

        while current is not None:
            if current.robot_id == robot_id:
                print("Robot found:")
                print(f"Robot ID: {current.robot_id}")
                print(f"Type: {current.type}")
                print(f"Price: {current.price}")
                print(f"Ranged: {current.ranged}")
                print(f"Camera: {current.camera}")
                return
            current = current.next_robot

        print("Robot not found")

def generate_robot_id():
    # Generate a random robot ID
    return ''.join(random.choices('0123456789ABCDEF', k=6))


def generate_robots(n):
    robots = []

    for _ in range(n):
        robot_id = generate_robot_id()
        t = random.choice(["AGV", "AFV", "ASV", "AUV"])
        price = random.uniform(0, 1000)
        ranged = random.randint(0, 100)
        camera = random.random()

        robots.append(Robot(robot_id, t, price, ranged, camera))
    return robots


def show_robots(robot_fleet):
    current = robot_fleet.head
    while current is not None:
        print(f"Robot ID: {current.robot_id}, Type: {current.type}, Price: {current.price}, Ranged: {current.ranged}, Camera: {current.camera}")
        current = current.next_robot


def main():
    robot_fleet = RobotFleet()
    control = 'e'

    while control != 'q':
        print("Aktualny stan floty robotów:")
        show_robots(robot_fleet)

        control = input("Możesz dodać robota (opcja: a), usunąć robota (opcja: r), wyszukać robota (opcja: f), wyjść (opcja: q)\nWybór:")

        if control == 'a':
            robot = generate_robots(1)[0]
            robot_fleet.add_robot(robot)
            print("Robot dodany")

        if control == 'r':
            robot_id = input("Podaj ID robota do usunięcia: ")
            robot_fleet.remove_robot(robot_id)

        if control == 'f':
            robot_id = input("Podaj ID robota do wyszukania: ")
            robot_fleet.find_robot(robot_id)

if __name__ == "__main__":
    main()

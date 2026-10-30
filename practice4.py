class SpaceShip:
    def __init__(self, fuel, hull, speed):
        self.fuel = fuel
        self.hull = hull
        self.speed = speed

    def fly(self, distance):
        if self.fuel >= distance:
            self.fuel -= distance
            print(f"Корабль пролетел {distance} км.")
        else:
            print("Недостаточно топлива")

    def info(self):
        print(
            f"Топливо: {self.fuel}, состояние корпуса: {self.hull}, "
            f"скорость: {self.speed} км/ч."
        )


class CrewMember:
    def __init__(self, name, health, skill, role):
        self.name = name
        self.health = health
        self.skill = skill
        self.role = role

    def info(self):
        print(
            f"Имя: {self.name}, здоровье: {self.health}, "
            f"навык: {self.skill}, роль: {self.role}."
        )


class Mission:
    def __init__(self, name, goal, resources):
        self.name = name
        self.goal = goal
        self.resources = resources
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def info(self):
        print(
            f"Миссия: {self.name}, цель: {self.goal}, "
            f"ресурсы: {self.resources}."
        )
        print(f"События: {', '.join(self.events)}")

class Vehicle:
    def __init__(self, owner_name, max_speed, mileage):
        self.owner_name = owner_name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        print(
            f"Владелец: {self.owner_name}, "
            f"максимальная скорость: {self.max_speed} км/ч, "
            f"пробег: {self.mileage} км."
        )


class Car(Vehicle):
    def __init__(self, owner_name, max_speed, mileage, make, model):
        super().__init__(owner_name, max_speed, mileage)
        self.make = make
        self.model = model

    def print_info(self):
        print(f"Легковой автомобиль {self.make} {self.model}, "
              f"владелец {self.owner_name}, максимальная скорость "
              f"{self.max_speed} км/ч, пробег {self.mileage} км.")


class Truck(Vehicle):
    def __init__(self, owner_name, max_speed, mileage, cargo_capacity):
        super().__init__(owner_name, max_speed, mileage)
        self.cargo_capacity = cargo_capacity

    def print_info(self):
        print(f"Грузовой автомобиль, владелец компания - {self.owner_name}, "
              f"максимальная скорость {self.max_speed} км/ч, "
              f"пробег {self.mileage} км, грузоподъемность "
              f"{self.cargo_capacity} кг.")


class Motorcycle(Vehicle):
    def __init__(self, owner_name, max_speed, mileage, model, motorcycle_gang):
        super().__init__(owner_name, max_speed, mileage)
        self.motorcycle_gang = motorcycle_gang
        self.model = model

    def print_info(self):
        print(f"Мотоцикл {self.model}, владелец {self.owner_name} "
              f"из {self.motorcycle_gang}, "
              f"максимальная скорость {self.max_speed} км/ч, "
              f"пробег {self.mileage} км")


car1 = Car("Иванов", 180, 50000, "Toyota", "Camry")
truck1 = Truck("wb", 120, 100000, 5000)
motorcycle1 = Motorcycle("Сидоров", 200, 20000, "Honda", "Hell's Angels")

vehicles = [car1, truck1, motorcycle1]

for vehicle in vehicles:
    vehicle.print_info()

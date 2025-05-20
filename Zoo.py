# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации
# о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
# между запусками программы.

import json

class Animal:
    def __init__(self, name, age, habitat="Unknown"):
        self.name = name
        self.age = age
        self.habitat = habitat

    def make_sound(self):
        pass

    def make_eat(self):
        return f"{self.name} ест."

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} издает мяу! возраст {self.age}"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} издает рык! возраст {self.age}, среда: {self.habitat}"

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} издает тыр-тыр! возраст {self.age}"

def animal_sound(animal):
    print(animal.make_sound())

# Классы сотрудников
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк.")

    def get_animals(self):
        return self.animals

    def get_employees(self):
        return self.employees

    def save_to_file(self):
        data = {
            "animals": [
                {"type": animal.__class__.__name__, **animal.__dict__}
                for animal in self.animals
            ],
            "employees": [
                {"type": employee.__class__.__name__, **employee.__dict__}
                for employee in self.employees
            ]
        }
        with open("zoo_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self):
        class_map = {
            "Animal": Animal,
            "Mammal": Mammal,
            "Reptile": Reptile,
            "Bird": Bird,
            "Employee": Employee,
            "ZooKeeper": ZooKeeper,
            "Veterinarian": Veterinarian
        }
        with open("zoo_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            self.animals = [
                class_map[animal["type"]](**{k: v for k, v in animal.items() if k != "type"})
                for animal in data["animals"]
            ]
            self.employees = [
                class_map[employee["type"]](**{k: v for k, v in employee.items() if k != "type"})
                for employee in data["employees"]
            ]

class ZooKeeper(Employee):
    def feed_animal(self):
        print(f"{self.name} кормит животное.")

class Veterinarian(Employee):
    def feed_animal(self):
        print(f"{self.name} лечит животное.")

    def heal_animal(self):
        print(f"{self.name} проводит осмотр животного.")

# Создание зоопарка
my_Zoo = Zoo()

# Добавление животных (корректные объекты, без проверок)
my_Zoo.add_animal(Mammal("Кот", 3))
my_Zoo.add_animal(Mammal("Собака", 5))
my_Zoo.add_animal(Reptile("Лиса", 2, "лес"))

# Добавление сотрудников

zookeeper = ZooKeeper("Виталик", 30)
veterinarian = Veterinarian("Василиса", 25)

new_employee = Employee("Гоша", 50)
my_Zoo.add_employee(new_employee)

my_Zoo.add_employee(zookeeper)
my_Zoo.add_employee(veterinarian)

# Вывод животных
for animal in my_Zoo.get_animals():
    print(animal.name, animal.age)

# Звуки животных
for animal in my_Zoo.get_animals():
    animal_sound(animal)

# Сотрудники
for employee in my_Zoo.get_employees():
    print(employee.name, employee.age)

# Действия сотрудников
zookeeper.feed_animal()
veterinarian.feed_animal()
veterinarian.heal_animal()

# Сохранение информации о зоопарке в файл
my_Zoo.save_to_file()

# Загрузка информации о зоопарке из файла
my_Zoo.load_from_file()


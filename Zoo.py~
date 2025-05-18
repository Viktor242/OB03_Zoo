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
import os

# Класс Animal
class Animal:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name):
        self.name = name

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

# Добавление животных и сотрудников
    def add_animal(self, animal_name):
        animal = Animal(animal_name)
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_employee(self, employee_name):
        employee = Employee(employee_name)
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк.")

    def save_data(self, filename="my_zoo1"):
        """Сохраняет данные зоопарка в файл"""
        data = {
            "animals": [animal.name for animal in self.animals],
            "employees": [emp.name for emp in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Данные зоопарка сохранены в файл {filename}")

    def load_data(self, filename="my_zoo1"):
        """Загружает данные зоопарка из файла"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
            self.animals = [Animal(animal) for animal in data["animals"]]
            self.employees = [Employee(emp) for emp in data["employees"]]
            print(f"Данные зоопарка загружены из файла {filename}")

# Кормление животных
class ZooKeeper(Employee):  # Наследуем от Employee
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal_name, zoo):
        for animal in zoo.animals:
            if animal.name == animal_name:
                print(f"{self.name} кормит {animal.name}.")
                return
        print(f"Животное {animal_name} не найдено в зоопарке.")

# Лечение животных
class Veterinarian(Employee):  # Наследуем от Employee
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal_name, zoo):
        for animal in zoo.animals:
            if animal.name == animal_name:
                print(f"{self.name} лечит {animal.name}.")
                return
        print(f"Животное {animal_name} не найдено в зоопарке.")


my_Zoo = Zoo()

# Добавление животных
my_Zoo.add_animal("Кот")
my_Zoo.add_animal("Собака")
my_Zoo.add_animal("Лиса")

# Добавление сотрудников
my_Zoo.add_employee("Виталик")
my_Zoo.add_employee("Василиса")

# Кормление животных
keeper = ZooKeeper("Виталик")
keeper.feed_animal("Кот", my_Zoo)

# Лечение животных
veterinarian = Veterinarian("Василиса")
veterinarian.feed_animal("Собака", my_Zoo)

# Сохранение данных в файл
my_Zoo.save_data()

# Загрузка данных из файла
my_Zoo.load_data()



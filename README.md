# 🦁 Zoo Management System 🐘

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Управление зоопарком с системой классов животных и персонала. Проект демонстрирует принципы ООП и модульности в Python.

## 📦 Модули

| Модуль       | Описание                          |
|--------------|-----------------------------------|
| `animal.py`  | Иерархия классов животных (Bird, Mammal, Reptile) |
| `zoo.py`     | Логика работы зоопарка (добавление животных/сотрудников, сохранение данных) |

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-repo/zoo-system.git
Импортируйте модули:

python
from animal import Bird, Mammal
from zoo import Zoo
Пример использования:

python
my_zoo = Zoo()
my_zoo.add_animal(Bird("Попугай", 3, "тропики"))
my_zoo.add_employee("Иван Соколов")
my_zoo.save_to_json("zoo_data.json")
📌 Key Features
animal.py
✅ Наследование (Animal → Bird/Mammal/Reptile)

✅ Полиморфизм (переопределение make_sound())

✅ Учет среды обитания (habitat)

zoo.py
✅ Управление коллекциями (животные + сотрудники)

✅ Сериализация в JSON

✅ Взаимодействие между классами

📚 Подробная документация
Модуль	Ссылка
animal.py	Документация
zoo.py	Документация
🛠 Зависимости
Python 3.6+

Нет внешних зависимостей

🏗️ Структура проекта
zoo-system/
├── animal.py           # Классы животных
├── zoo.py              # Логика зоопарка
├── README.md           # Этот файл
└── docs/
    ├── animal.md       # Детали animal.py
    └── zoo.md          # Детали zoo.py
👨‍💻 Разработка
Для добавления нового типа животных:

Создайте класс в animal.py (наследуясь от Animal)

Добавьте тесты в tests/

Для расширения функционала зоопарка:

Модифицируйте zoo.py

Обновите документацию в docs/zoo.md

📜 Лицензия
MIT License. Подробнее в файле LICENSE.

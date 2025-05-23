# 🦁 Zoo Management System

Простое консольное приложение на Python для моделирования работы зоопарка. Позволяет добавлять животных и сотрудников, выполнять базовые действия (звуки, кормление, лечение), а также сохранять и загружать данные в/из JSON-файла.

## 📂 Структура проекта

### Животные:

- `Animal` — базовый класс.
- `Mammal`, `Reptile`, `Bird` — подклассы с уникальной реализацией звуков.

### Сотрудники:

- `Employee` — базовый класс.
- `ZooKeeper` — смотритель зоопарка, может кормить животных.
- `Veterinarian` — ветеринар, умеет лечить и кормить животных.

### Зоопарк:

- `Zoo` — управляет коллекциями животных и сотрудников, поддерживает добавление, просмотр, сохранение и загрузку данных.

## ✅ Возможности

- Добавление животных и сотрудников;
- Вывод информации о зоопарке;
- Проигрывание звуков животных;
- Кормление и лечение животных;
- Сохранение и загрузка данных в формате JSON.

## 💾 Сохранение данных

Все данные сохраняются в файл `zoo_data.json`. При запуске можно загрузить предыдущую сохранённую структуру зоопарка.

## 🛠️ Требования

- Python версии 3.6 или выше.

## 📌 Примечания

- Используется стандартная библиотека `json` для сериализации;
- При добавлении новых подклассов необходимо обновить карту классов `class_map` для корректной загрузки;
- Валидация данных и проверка типов не реализованы — данные добавляются напрямую.

import requests

# Определение нового элемента задачи
новая_задача = {
    "userId": 1,
    "title": "Завершить задание",
    "completed": False
}

# Отправка POST-запроса для создания нового элемента задачи
url_post = "https://jsonplaceholder.typicode.com/todos"
ответ_post = requests.post(url_post, json=новая_задача)

# Вывод содержимого ответа POST-запроса
print("Содержимое ответа POST:")
print(ответ_post.content)

# Проверка кода состояния
if ответ_post.status_code in range(400, 600):
    print(f"Ошибка: {ответ_post.status_code} - {ответ_post.reason}")

# Редактирование некоторых данных созданного элемента задачи (например, изменение статуса выполнения)
if ответ_post.status_code == 201:  # Предполагается, что код состояния 201 указывает на успешное создание
    созданная_задача = ответ_post.json()
    print(созданная_задача)

    # Редактирование некоторых данных
    созданная_задача["completed"] = True

    # Отправка PUT-запроса для обновления элемента задачи
    url_put = f"https://jsonplaceholder.typicode.com/todos/{созданная_задача['id']}"
    ответ_put = requests.put(url_put, json=созданная_задача)

    # Вывод содержимого ответа PUT-запроса
    print("\nСодержимое ответа PUT:")
    print(ответ_put.content)

    # Проверка кода состояния
    if ответ_put.status_code in range(400, 600):
        print(f"Ошибка: {ответ_put.status_code} - {ответ_put.reason}")
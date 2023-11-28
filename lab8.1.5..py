import requests

# 1.1: GET-запрос
post_id = 1
url_get = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response_get = requests.get(url_get)

# Вывод содержимого ответа (JSON)
print("1.1: JSON ответ:")
print(response_get.json())

# Проверка статус-кода GET-запроса
if 400 <= response_get.status_code <= 599:
    print(f"1.1: Ошибка - Код состояния: {response_get.status_code}")

# 1.2: Создание класса "ToDo"
class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# Создание объекта с указанным id
to_do_object = ToDo(**response_get.json())

# Вывод атрибутов объекта
print("\n1.2: Атрибуты объекта ToDo:")
print(f"userId: {to_do_object.userId}")
print(f"id: {to_do_object.id}")
print(f"title: {to_do_object.title}")
print(f"completed: {to_do_object.completed}")

# 1.3: Создание нового объекта класса ToDo
new_to_do_object = ToDo(userId=2, id=101, title='New Task', completed=False)

# Вывод атрибутов нового объекта
print("\n1.3: Атрибуты нового объекта ToDo:")
print(f"userId: {new_to_do_object.userId}")
print(f"id: {new_to_do_object.id}")
print(f"title: {new_to_do_object.title}")
print(f"completed: {new_to_do_object.completed}")

# 1.4: POST-запрос
url_post = 'https://jsonplaceholder.typicode.com/todos'
new_todo_item = {
    "userId": new_to_do_object.userId,
    "title": new_to_do_object.title,
    "completed": new_to_do_object.completed
}

response_post = requests.post(url_post, json=new_todo_item)
print("\n1.4: JSON ответ POST-запроса:")
print(response_post.json())

# Проверка статус-кода POST-запроса
if 400 <= response_post.status_code <= 599:
    print(f"1.4: Ошибка - Код состояния: {response_post.status_code}")

# Извлечение ID из ответа POST-запроса
new_todo_id = response_post.json()["id"]

# 1.5: Редактирование данных атрибутов todo item
edited_todo_item = {
    "userId": new_to_do_object.userId,
    "title": "Updated Title",
    "completed": True
}

# PUT-запрос для обновления данных
url_put = f'https://jsonplaceholder.typicode.com/todos/{new_todo_id}'
response_put = requests.put(url_put, json=edited_todo_item)

# Вывод содержимого ответа (JSON) от PUT-запроса
print("\n1.5: JSON ответ PUT-запроса:")
print(response_put.json())

# Проверка статус-кода PUT-запроса
if 400 <= response_put.status_code <= 599:
    print(f"1.5: Ошибка - Код состояния: {response_put.status_code}")
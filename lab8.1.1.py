import requests

# URL для GET-запроса, замените {post_id} на нужный идентификатор
url = 'https://jsonplaceholder.typicode.com/todos/1'

# Выполнение GET-запроса
response = requests.get(url)

# Вывод содержимого ответа в формате JSON
print("Response JSON:")
print(response.json())

# Проверка статус-кода
if 400 <= response.status_code <= 599:
    print(f"Error: {response.status_code}")


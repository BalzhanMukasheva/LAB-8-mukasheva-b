import requests

# Задаем идентификатор, который будет использоваться в запросе
custom_id = 1

# Формируем конечную точку (URL) для запроса на основе идентификатора
endpoint = f'https://jsonplaceholder.typicode.com/todos/{custom_id}'

# Выполняем GET-запрос к указанной конечной точке
response = requests.get(endpoint)

# Выводим содержимое ответа в формате JSON
print(response.json())

# Проверяем, если код состояния (HTTP status code) находится в диапазоне 400–499 или 500–599, то выводим сообщение об ошибке
if response.status_code >= 400:
    print(f"Произошла нештатная ситуация: {response.status_code} - {response.text}")
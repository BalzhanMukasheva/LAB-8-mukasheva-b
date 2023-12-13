import requests

# Замените chosen_id на выбранный идентификатор задачи
идентификатор_задачи = 1

# Изменяем значение в словаре, представляющем элемент задачи
обновленная_задача["title"] = "ANOTHER NEW"

# Выполняем PUT-запрос для обновления задачи
url_put = f'https://jsonplaceholder.typicode.com/todos/{идентификатор_задачи}'
ответ_put = requests.put(url_put, json=обновленная_задача)

# Печать содержимого ответа PUT-запроса
print(ответ_put.json())

# Проверка кода состояния
if ответ_put.status_code >= 400:
    print(f"Ошибка: {ответ_put.status_code} - {ответ_put.text}")
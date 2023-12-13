import requests
import random

# Генерируем случайный идентификатор персонажа
cartoon_id = random.randint(1, 826)

# Выполняем GET-запроса к API
url = f"https://rickandmortyapi.com/api/character/{cartoon_id}"
rsp = requests.get(url)

# Проверяем успешность запроса (код состояния 200)
if rsp.status_code == 200:
    # Выводим ответ в формате JSON
    json_rsp = rsp.json()
    print(json_rsp)

    # Отображение ключей структуры JSON
    keys = json_rsp.keys()
    print(f"\nКлючи структуры JSON: {keys}")
else:
    print(f"Ошибка. Код состояния: {rsp.status_code}")





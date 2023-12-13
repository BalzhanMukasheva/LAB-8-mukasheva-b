# Определение класса ToDo для представления задачи
class ToDo:
    # Конструктор класса, вызывается при создании нового объекта ToDo
    def __init__(self, userId, id, title, completed):
        # Инициализация атрибутов объекта значениями, переданными при создании
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# Используем тот же идентификатор задачи (post_id), что и ранее
post_id = 1

# Создание нового объекта ToDo с определенными значениями атрибутов
todo_sm = ToDo(userId=1, id=post_id, title="Пример Заголовка", completed=False)

# Вывод информации о созданной задаче, используя значения атрибутов объекта
print(f"Идентификатор пользователя: {todo_sm.userId}")
print(f"Идентификатор задачи: {todo_sm.id}")
print(f"Заголовок задачи: {todo_sm.title}")
print(f"Завершена ли задача: {todo_sm.completed}")
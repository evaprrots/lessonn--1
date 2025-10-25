from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title               
        self.description = description    
        self.deadline = deadline         
        self.completed = False            

    def mark_completed(self):
        self.completed = True

    def get_info(self):
        status = "Виконано" if self.completed else  "Не виконано"
        return f"{self.title} | {self.description} | Дедлайн: {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано!")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено!")
                return
        print(f"Завдання '{title}' не знайдено!")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Завдання '{title}' відмічено як виконане!")
                return
        print(f"Завдання '{title}' не знайдено!")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return
        print("\Список завдань:")
        for task in self.tasks:
            print(" -", task.get_info())

if __name__ == "__main__":
    manager = TaskManager()

    task1 = Task("Вивчити Python", "Пройти 5 уроків", "2025-10-30")
    task2 = Task("Написати звіт", "Звіт по проекту AI", "2025-10-25")

    manager.add_task(task1)
    manager.add_task(task2)

    manager.show_tasks()
    manager.complete_task("Вивчити Python")
    manager.remove_task("Написати звіт")
    manager.show_tasks()

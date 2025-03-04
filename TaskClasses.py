#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, due_date, status=0):
        self.description = description
        self.due_date = due_date
        self.status = status #задача не выполнена - 0, выполнена - 1

    def mark_done(self):
        self.status = 1 # отметка задачи как выполненной
        print(f"Задача '{self.description}' выполнена!")

    def mark_not_done(self):
        self.status = 0  # отметка задачи как невыполненной
        print(f"Задача '{self.description}' выполнена!")

    @staticmethod
    def print_pending_tasks(task_list): #метод для вывода всех невыполненных задач
        pending_tasks = [task for task in task_list if task.status == 0]
        if pending_tasks:
            print("Текущие задачи (не выполненные): ")
            for task in pending_tasks:
                print(f' - {task.description}, срок выполения: {task.due_date}')
        else:
            print('Все задачи выполнены!')

task_list = [] # список задач
# создание задач
task1 = Task('Задача 1: закончить отчет', '2025-03-05')
task2 = Task('Задача 2: урок английского', '2025-03-04')
task3 = Task('Задача 3: заметка для блога', '2025-03-07')

# добавление задач в список
task_list.append(task1)
task_list.append(task2)
task_list.append(task3)

# отметим одну задачу как выполненную
task1.mark_done()

# вывод текущих невыполненных задач
Task.print_pending_tasks(task_list)
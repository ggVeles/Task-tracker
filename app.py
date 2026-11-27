from file_manager import save_tasks, load_tasks
from datetime import datetime

tasks = load_tasks()
task_text = input("Введи задачу: ")

new_task = {
    "title": task_text,
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
}
tasks.append(new_task)

save_tasks(tasks)

for i in tasks:
    print(i)
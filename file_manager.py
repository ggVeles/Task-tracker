import json

def save_tasks(tasks_list):
    with open('tasks.json', "w", encoding='utf-8') as file:
        json.dump(tasks_list, file, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

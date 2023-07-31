import os
import json


def list_tasks(tasks):
    print()
    if not tasks:
        print('There is no task to list')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, redo_tasks):
    print()
    if not tasks:
        print('There is no task to undo')
        return

    task = tasks.pop()
    print(f'{task=} removed from task list')
    redo_tasks.append(task)
    print()
    list_tasks(tasks)


def redo(tasks, redo_tasks):
    print()
    if not redo_tasks:
        print('There is no task to redo')
        return

    task = redo_tasks.pop()
    print(f'{task=} added to task list')
    tasks.append(task)
    print()
    list_tasks(tasks)


def add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You did not add any task')
        return
    print(f'{task=} added to task list')
    tasks.append(task)
    print()
    list_tasks(tasks)


def read(tasks, file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('File does not exist')
        save(tasks, file_path)
    return data


def save(tasks, file_path):
    data = tasks
    with open(file_path, 'w', encoding='utf8') as file:
        data = json.dump(tasks, file, indent=2, ensure_ascii=False)
    return data


FILE_PATH = 'aula119.json'
tasks = read([], FILE_PATH)
redo_tasks = []

while True:
    print('Commands: list, undo e redo')
    task = input('Input a task or a command: ')

    commands = {
        'list': lambda: list_tasks(tasks),
        'undo': lambda: undo(tasks, redo_tasks),
        'redo': lambda: redo(tasks, redo_tasks),
        'clear': lambda: os.system('clear'),
        'add': lambda: add(task, tasks),
    }
    command = commands.get(task) if commands.get(task) is not None else \
        commands['add']
    command()
    save(tasks, FILE_PATH)

    # if task == 'list':
    #     list_tasks(tasks)
    #     continue
    # elif task == 'undo':
    #     undo(tasks, redo_tasks)
    #     list_tasks(tasks)
    #     continue
    # elif task == 'redo':
    #     redo(tasks, redo_tasks)
    #     list_tasks(tasks)
    #     continue
    # elif task == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     add(task, tasks)
    #     list_tasks(tasks)
    #     continue
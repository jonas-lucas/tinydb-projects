# Main script of Task Manager project

import os
import shutil
import platform
import sys

try:
    from tinydb import TinyDB, Query
    from tinydb.table import Table
    from tinydb.storages import MemoryStorage
except ImportError:
    print('Packege "tinydb" is not installed.')
    exit()

# CRUD


def create_task(name: str) -> None:
    """Create a new task."""
    tasks.insert({'name': name, 'mark': False})


def list_tasks(n: int) -> None:
    """List a n numbers of task."""
    for task, index in zip(sorted(tasks.all(), key=lambda task: task['name']), range(n)):
        print(str('(x) ' if task['mark'] else '( ) ' + task['name']).ljust(30).center(size().columns))


def select_task(name: str) -> None:
    """Select a unique task by name."""
    sorted_tasks = sorted(tasks.all(), key=lambda task: task['name'])
    if sorted_tasks:
        print('(x)' if sorted_tasks[0]['mark'] else '( )', sorted_tasks[0]['name'])


def delete_task(id: int) -> None:
    """Delete a unique task by id."""
    tasks.remove(doc_ids=[id])
    print('Removed')


# Command Line Interface
def create_task_interface() -> str:
    header('CREATE TASK')
    task_name = input('Enter the name of the new task: ').title().strip()
    create_task(task_name)
    return f'Created "{task_name}" as a new task'


def list_tasks_interface() -> str:
    header('LIST TASKS')
    list_tasks(size().lines // 2)
    input()


def size() -> int:
    return shutil.get_terminal_size()


def header(title: str = '<INSERT TEXT>') -> None:
    if platform.system() == 'Linux':
        os.system('clear')

    print('=' * size().columns)
    print(title.center(size().columns))
    print('=' * size().columns)
    print()


def init() -> None:
    try:
        feedback: str = ''
        while True:
            header('HOME PAGE')
            print('[1] - Create a new task'.ljust(30).center(size().columns))
            print('[2] - List tasks'.ljust(30).center(size().columns))
            print()
            print('[0] - Quit'.ljust(30).center(size().columns))
            print()
            if feedback:
                print(feedback)
            command: str = input('Write your command: ').lower().strip()

            if command == '':
                feedback = ''
                continue
            elif '0' in command or command in 'quit':
                break
            elif '1' in command or command in 'create a new task':
                feedback = create_task_interface()
            elif '2' in command or command in 'list tasks':
                feedback = list_tasks_interface()
    except KeyboardInterrupt:
        print()
        exit()


def main() -> None:
    global tasks

    if 'dev' in sys.argv:
        database: TinyDB = TinyDB(storage=MemoryStorage)
    else:
        database: TinyDB = TinyDB(
            'tasks.json', sort_keys=True, 
            indent=4, separators=(',', ': ')
        )

    tasks = database.table('tasks')


if __name__ == '__main__':
    main()
    init()

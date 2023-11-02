# Main script of Task Manager project

from sys import argv

try:
    from tinydb import TinyDB, Query
    from tinydb.table import Table
    from tinydb.storages import MemoryStorage
except ImportError:
    print('Packege "tinydb" is not installed.')
    exit()

# CRUD


def create_task(description: str) -> None:
    """Create a new task."""
    tasks.insert({'description': description, 'mark': False})


def search_task(description: str) -> None:
    """Search task by description."""
    for task in sorted(tasks.all(), key=lambda task: task['description']):
        if description in task['description']:
            print('(x)' if task['mark'] else '( )', task['description'])


def select_task(id: int) -> None:
    """Select a unique task by id."""
    task = tasks.get(doc_id=id)
    print(task.doc_id, task['description'])


def delete_task(id: int) -> None:
    """Delete a unique task by id."""
    tasks.remove(doc_ids=[id])
    print('Removed')


if __name__ == '__main__':
    if 'dev' in argv:
        database: TinyDB = TinyDB(storage=MemoryStorage)
    else:
        database: TinyDB = TinyDB(
            'tasks.json', sort_keys=True, indent=4, separators=(',', ': '))

    tasks: Table = database.table('tasks')

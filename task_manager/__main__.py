# Main script of Task Manager project
 	
try:
	from tinydb import TinyDB
except ImportError:
	print('Packege "tinydb" is not installed.')
	exit()

# CRUD
def create_task(description: str) -> None:
	"""Create a new task."""
	database.insert({'description': description})

def read_task(description: str) -> None:
	"""Read task by description."""
	for task in database.all():
		if description in task['description']:
			print(task)

if __name__ == '__main__':
	database: TinyDB = TinyDB('tasks.json')


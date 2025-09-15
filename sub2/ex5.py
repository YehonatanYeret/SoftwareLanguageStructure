def task_manager():
    tasks = {}

    def add_task(name, state="incomplete"):
        tasks[name] = state

    def get_tasks():
        return tasks.copy()

    def complete_task(name):
        if name in tasks:
            tasks[name] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


def main():
    # Create a new task manager
    tasks_manager = task_manager()
    # Add tasks
    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")
    # Get the list of tasks
    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)
    # Should print: {'Write email': 'incomplete', 'Shopping': 'in progress', 'Homework':'incomplete'}
    # Mark a task as complete
    tasks_manager['complete_task']("Write email")
    # Get the list of tasks after marking and deleting
    current_tasks = tasks_manager['get_tasks']()
    print(current_tasks)
    # Should print: {'Write email': 'complete', 'Shopping': 'in progress', 'Homework': 'incomplete'}


if __name__ == '__main__':
    main()

# print("1.Add a task")
# print("2.mark as completed")
# print("3.view list")
# print("4.remove task")
# print("5.exit")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def mark_as_completed(self, task):
        if task in self.tasks:
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found.')

    def view_list(self):
        if not self.tasks:
            print('To-Do List is empty.')
        else:
            print('To-Do List:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed successfully.')
        else:
            print(f'Task "{task}" not found.')

def main():
    todo_list = ToDoList()

    while True:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Mark as Completed')
        print('3. View List')
        print('4. Remove Task')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to mark as completed: ')
            todo_list.mark_as_completed(task)
        elif choice == '3':
            todo_list.view_list()
        elif choice == '4':
            task = input('Enter the task to remove: ')
            todo_list.remove_task(task)
        elif choice == '5':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()


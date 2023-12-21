class TodoList:
    def _init_(self):
        self.tasks = []
        self.next_task_id = 1

    def add_task(self, task):
        self.tasks.append({"id": self.next_task_id, "task": task, "completed": False})
        self.next_task_id += 1

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False

    def get_tasks(self):
        return self.tasks

    def remove_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return True
            return False
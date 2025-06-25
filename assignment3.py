# Task class
class Task:
    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = duration
        self.priority = priority

    def __str__(self):
        return f"Title: {self.title}, Duration: {self.duration} mins, Priority: {self.priority}"

# Queue functions
def insert(queue, task):
    queue.append(task)

def extract(queue):
    if not is_empty(queue):
        return queue.pop(0)
    return None

def peek(queue):
    if not is_empty(queue):
        return queue[0]
    return None

def is_empty(queue):
    return len(queue) == 0

# Task Functions
# Extract highest priority task and remove it when completed
def complete_next_task(queue):
    if is_empty(queue):
        print("No tasks in the queue.")
        return None

    # Find task with highest priority (lowest number)
    highest_priority_task = queue[0]
    for task in queue:
        if task.priority < highest_priority_task.priority:
            highest_priority_task = task

    print("\nNext task to complete:")
    print(highest_priority_task)

    # Ask user if they want to complete it
    answer = input("Do you want to mark this task as completed? (yes/no): ").strip().lower()
    if answer == "yes":
        queue.remove(highest_priority_task)
        print("Task removed from the queue.")
    else:
        print("Task was not removed.")

    return highest_priority_task

# Search for task
def search_for_task(queue, title):
    sorted_queue = sorted(queue, key=lambda t: t.title)
    low, high = 0, len(sorted_queue) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_queue[mid].title == title:
            print("Task found:")
            print(sorted_queue[mid])
            return sorted_queue[mid]
        elif sorted_queue[mid].title < title:
            low = mid + 1
        else:
            high = mid - 1

    print("Task not found.")
    return None

# Sorting Tasks by duration ascending
def sort_tasks(queue):
    return sorted(queue, key=lambda t: t.duration)


# Input + Execution

task_queue = []

num_tasks = int(input("How many tasks do you want to create? "))

for i in range(num_tasks):
    print(f"\nTask {i+1}:")
    title = input("Enter task title: ")
    duration = int(input("Enter duration (minutes): "))
    priority = int(input("Enter priority (lower number = higher priority): "))
    insert(task_queue, Task(title, duration, priority))

print("\nAll tasks entered:")
for task in task_queue:
    print(task)

print("\n--- Complete Next Task ---")
complete_next_task(task_queue)

search_title = input("\nEnter a title to search for: ")
search_for_task(task_queue, search_title)

print("\nTasks sorted by duration:")
sorted_tasks = sort_tasks(task_queue)
for task in sorted_tasks:
    print(task)

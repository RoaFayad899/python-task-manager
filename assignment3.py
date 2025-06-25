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

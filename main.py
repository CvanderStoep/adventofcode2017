from collections import deque

# Create a deque of tasks
tasks = deque(["Task 1", "Task 2", "Task 3", "Task 4"])

# Process tasks in a round-robin fashion
# for _ in range(8):  # Process tasks multiple times
#     current_task = tasks.popleft()  # Fetch the first task
#     print(f"Processing {current_task}")
#     tasks.append(current_task)  # Move the completed task to the end

for _ in range(8):  # Process tasks multiple times
    current_task = tasks[0]  # Fetch the first task
    print(f"Processing {current_task}")
    tasks.rotate(-1)  # Move the completed task to the end
    print(tasks)
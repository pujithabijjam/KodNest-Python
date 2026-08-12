def add_task(task, tasks = []):
    if task is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("Learn Python"))
print(add_task("practice Functions"))

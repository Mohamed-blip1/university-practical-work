1. Replace dicts with a Task class:
class Task:
    def __init__(self, name, priority, done=False):
        ...

2. Add:
due dates
priority update
JSON storage

3. Replace manual tests with pytest

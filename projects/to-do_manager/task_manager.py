import os
from enum import Enum

class Choice(Enum):
    ALL = 0
    COMPLETED = 1
    UNCOMPLETED = 2
    
class TaskManager:
    def __init__(self):    
        self.tasks={}
        self.keys_sorted_by_priority=[]
        self.SORTED=True
        self.UP_TO_DATE=True
        self.MODIFIED_ITEM=False

    def add_task(self, task_name: str, priority: int) -> bool:
        if task_name in self.tasks:
            return False

        self.tasks[task_name]={"done":False,"priority":priority}
        self.keys_sorted_by_priority.append((priority,task_name))

        self.MODIFIED_ITEM=True
        self.UP_TO_DATE=False
        self.SORTED=False

        return True

    def get_tasks(self, choice :int) -> list:
        """
        Choices are : ALL(0), COMPLETED(1), UNCOMPLETED(2)
        Returns [(task_name, info),...]
        """

        self.refresh_keys()
        self.sort_keys()

        if choice == Choice.ALL.value:
            return [(task_name, self.tasks[task_name]) for _, task_name in self.keys_sorted_by_priority]
        else:
            status = (choice == Choice.COMPLETED.value)
            return [(task_name, self.tasks[task_name]) for _, task_name in self.keys_sorted_by_priority
                                                        if  self.tasks[task_name]["done"]==status]

    def refresh_keys(self, force : bool =False):

        if self.MODIFIED_ITEM or force:
            self.keys_sorted_by_priority.clear()
            self.keys_sorted_by_priority.extend(
                (info["priority"], task_name) for task_name, info in self.tasks.items())

            self.MODIFIED_ITEM=False
            self.SORTED=False

    def sort_keys(self, force: bool =False):

        if not self.SORTED or force:
            self.keys_sorted_by_priority.sort()
            self.SORTED=True

    def get_tasks_by_keyword(self, keyword: str):
        
        self.refresh_keys()
        self.sort_keys()

        return [(task_name, self.tasks[task_name]) for _, task_name in self.keys_sorted_by_priority
                                                    if keyword.lower() in task_name.lower()]
    
    def edit_task_status(self, task_name: str, new_status: bool) -> bool:


        if task_name not in self.tasks:
            return False

        self.tasks[task_name]["done"] = new_status

        # If later were sorting based on "done" status
        # SORTED=False

        self.MODIFIED_ITEM=True
        self.UP_TO_DATE=False

        return True

    def edit_task_name(self, old_name: str, new_name: str) -> bool:
        """
        Renames a task. Returns True if successful, False otherwise
        """

        if old_name not in self.tasks or new_name in self.tasks:
            return False

        self.tasks[new_name] = self.tasks.pop(old_name)

        self.MODIFIED_ITEM=True
        self.UP_TO_DATE=False
        self.SORTED=False

        return True

    def delete_task(self, task_name: str) -> bool:

        if self.tasks.pop(task_name,None) is not None:
            self.UP_TO_DATE=False
            self.MODIFIED_ITEM=True
            self.SORTED=False
            return True

        return False
    
    def save_tasks(self, FILE_NAME) -> bool:

        self.refresh_keys(force=True)
        self.sort_keys(force=True)

        with open(FILE_NAME,"w") as file:
            for task_name, info in self.get_tasks(Choice.ALL.value): 
                file.write(task_name+":"+str(info["done"])+":"+str(info["priority"])+"\n")

        self.UP_TO_DATE=True

        return True

    def load_tasks(self, FILE_NAME) -> bool:

        if not os.path.exists(FILE_NAME):
            return False
        
        self.tasks.clear()
        with open(FILE_NAME,"r") as file:
            for line in file:
                line = line.strip()
                if line:
                    task_name, done_str, priority_str = line.split(":")
                    done= (done_str == "True")
                    priority= int(priority_str)
                    self.tasks[task_name]={"done":done,"priority":priority}

        self.refresh_keys(force=True)
        self.sort_keys(force=True)
        
        self.UP_TO_DATE=True

        return True    
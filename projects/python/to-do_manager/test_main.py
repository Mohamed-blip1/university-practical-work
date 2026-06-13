from task_manager import TaskManager
from task_manager import Choice
import os

FILE_NAME = "tasks_file.txt"

# Test sort_keys() and refresh_keys()--------------------------

def test_sort_keys():

    manager = TaskManager()

    manager.keys_sorted_by_priority.clear()

    manager.keys_sorted_by_priority.append((3,"priority 3"))
    manager.keys_sorted_by_priority.append((1,"priority 1"))
    manager.keys_sorted_by_priority.append((2,"priority 2"))

    manager.SORTED=False

    manager.sort_keys()

    assert manager.SORTED
    assert manager.keys_sorted_by_priority == [(1,"priority 1"),(2,"priority 2"),(3,"priority 3")]

    print("test_sorted_keys passe!")

def test_forced_sort_keys():

    manager = TaskManager()

    manager.keys_sorted_by_priority.clear()

    manager.keys_sorted_by_priority.append((3,"priority 3"))
    manager.keys_sorted_by_priority.append((1,"priority 1"))
    manager.keys_sorted_by_priority.append((2,"priority 2"))

    manager.SORTED=True

    manager.sort_keys(True)

    assert manager.SORTED
    assert manager.keys_sorted_by_priority == [(1,"priority 1"),(2,"priority 2"),(3,"priority 3")]

    print("test_forced_sorted_keys passe!")

test_sort_keys()
test_forced_sort_keys()
print("done testing sort_keys()")
print()

def test_refresh_keys():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.tasks["item3"]={"done":False,"priority":3}
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}

    manager.SORTED = True
    manager.MODIFIED_ITEM = True

    manager.refresh_keys()

    assert not manager.MODIFIED_ITEM
    assert not manager.SORTED
    assert manager.keys_sorted_by_priority == [(3,"item3"), (1,"item1"),(2,"item2")]

    print("test_refresh_keys passe!")

def test_forced_refresh_keys():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.tasks["item3"]={"done":False,"priority":3}
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}

    manager.SORTED = True
    manager.MODIFIED_ITEM = False

    manager.refresh_keys(True)

    assert not manager.MODIFIED_ITEM
    assert not manager.SORTED
    assert manager.keys_sorted_by_priority == [(3,"item3"), (1,"item1"),(2,"item2")]

    print("test_forced_refresh_keys passe!")

test_refresh_keys()
test_forced_refresh_keys()
print("done testing refresh_keys()")
print()

# Test add_task()--------------------------

def test_add_task():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.MODIFIED_ITEM = False
    manager.UP_TO_DATE = True
    manager.SORTED = True

    success = manager.add_task("math",2)

    assert success
    assert "math" in manager.tasks
    assert manager.tasks["math"]["done"] == False
    assert manager.tasks["math"]["priority"] == 2
    assert manager.keys_sorted_by_priority == [(2,"math")]

    assert manager.MODIFIED_ITEM == True
    assert manager.UP_TO_DATE == False
    assert manager.SORTED == False

    print("test_add_task passed!")

def test_add_duplicate_task():

    manager = TaskManager()
   
    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.tasks["python"]={ "done" : False, "priority" : 1 }
    manager.keys_sorted_by_priority.append((1,"python"))

    manager.MODIFIED_ITEM = False
    manager.UP_TO_DATE = True
    manager.SORTED = True

    success = manager.add_task("python",1)

    assert not success
    assert len(manager.tasks) == 1
    assert len(manager.keys_sorted_by_priority) == 1

    assert manager.MODIFIED_ITEM == False
    assert manager.UP_TO_DATE == True
    assert manager.SORTED == True

    print("test_add_duplicate_task passsed!")

test_add_task()
test_add_duplicate_task()
print("done testing add_task()")
print()

# Test get_tasks() and get_tasks_by_keyword() --------------------------

def test_get_tasks_all():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()
    
    manager.tasks["item3"]={"done":False,"priority":3}
    manager.keys_sorted_by_priority.append((3,"item3"))
    
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.keys_sorted_by_priority.append((1,"item1"))
    
    manager.tasks["item2"]={"done":True,"priority":2}
    manager.keys_sorted_by_priority.append((2,"item2"))

    manager.MODIFIED_ITEM = True
    manager.SORTED = False

    getted_tasks = manager.get_tasks(Choice.ALL)

    assert getted_tasks == [
        ("item1", {"done":False,"priority":1}),
        ("item2", {"done":True,"priority":2}),
        ("item3", {"done":False,"priority":3})
        ]

    print("test_get_tasks_all passed!")

def test_get_tasks_completed():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.tasks["item3"]={"done":True,"priority":3}
    manager.keys_sorted_by_priority.append((3,"item3"))

    manager.tasks["item1"]={"done":False,"priority":1}
    manager.keys_sorted_by_priority.append((1,"item1"))

    manager.tasks["item2"]={"done":True,"priority":2}
    manager.keys_sorted_by_priority.append((2,"item2"))

    manager.MODIFIED_ITEM = True
    manager.SORTED = False

    getted_tasks = manager.get_tasks(Choice.COMPLETED)

    assert getted_tasks == [
        ("item2", {"done":True,"priority":2}),
        ("item3", {"done":True,"priority":3})
        ]
    
    print("test_get_tasks_completed passed!")
    

def test_get_tasks_uncompleted():

    manager = TaskManager()

    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()
    
    manager.tasks["item3"]={"done":False,"priority":3}
    manager.keys_sorted_by_priority.append((3,"item3"))
    
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.keys_sorted_by_priority.append((1,"item1"))
    
    manager.tasks["item2"]={"done":True,"priority":2}
    manager.keys_sorted_by_priority.append((2,"item2"))

    manager.MODIFIED_ITEM = True
    manager.SORTED = False

    getted_tasks = manager.get_tasks(Choice.UNCOMPLETED)

    assert getted_tasks == [
        ("item1", {"done":False,"priority":1}),
        ("item3", {"done":False,"priority":3})
        ]

    print("test_get_tasks_uncompleted passed!")

test_get_tasks_all()
test_get_tasks_completed()
test_get_tasks_uncompleted()
print("done testing get_tasks()")
print()

# Test get_tasks_by_keyword()--------------------------

def test_get_tasks_by_keyword():

    manager = TaskManager()

    manager.tasks.clear()
    
    manager.tasks["item3"]={"done":False,"priority":3}
    manager.tasks["some3"]={"done":False,"priority":3}
    
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["some1"]={"done":False,"priority":1}

    manager.tasks["item2"]={"done":True,"priority":2}
    manager.tasks["some2"]={"done":True,"priority":2}

    manager.keys_sorted_by_priority.append((3,"item3"))
    manager.keys_sorted_by_priority.append((3,"some3"))

    manager.keys_sorted_by_priority.append((2,"item2"))
    manager.keys_sorted_by_priority.append((2,"some2"))
    
    manager.keys_sorted_by_priority.append((1,"item1"))
    manager.keys_sorted_by_priority.append((1,"some1"))

    manager.SORTED = False
    manager.MODIFIED_ITEM = True

    getted_tasks = manager.get_tasks_by_keyword("me")

    assert getted_tasks == [
        ("some1", {"done":False,"priority":1}),
        ("some2", {"done":True,"priority":2}),
        ("some3", {"done":False,"priority":3})
    ]

    print("test_get_tasks_by_keyword passed!")

test_get_tasks_by_keyword()
print("done testing get_tasks_by_keyword()")
print()

# Test edit_task_status()--------------------------

def test_edit_task_status():

    manager = TaskManager()

    manager.tasks.clear()

    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}
    
    manager.UP_TO_DATE = True
    manager.MODIFIED_ITEM = False

    # Task does not exist case
    case1 = manager.edit_task_status("some",True)
    
    assert not case1
    assert manager.tasks.get("some") == None

    assert manager.UP_TO_DATE == True
    assert manager.MODIFIED_ITEM == False
    
    case2 = manager.edit_task_status("item1",True)
    case3 = manager.edit_task_status("item2",False)
    
    assert case2
    assert case3
    assert manager.tasks["item1"] == {"done":True,"priority":1}
    assert manager.tasks["item2"] == {"done":False,"priority":2}
    
    assert manager.UP_TO_DATE == False
    assert manager.MODIFIED_ITEM == True

    print("test_edit_task_status passed!")

test_edit_task_status()
print("done testing edit_task_status()")
print()

# Test edit_task_name()--------------------------

def test_edit_task_name():

    manager = TaskManager()
   
    manager.tasks.clear()
    manager.keys_sorted_by_priority.clear()

    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}
    manager.tasks["item3"]={"done":False,"priority":3}

    old_tasks = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    manager.MODIFIED_ITEM=False
    manager.UP_TO_DATE=True
    manager.SORTED=True

    # Not existing task case
    case1 = manager.edit_task_name("","some")
    
    tasks_case1 = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    assert tasks_case1 == old_tasks
    assert not case1
    assert manager.MODIFIED_ITEM == False
    assert manager.UP_TO_DATE == True
    assert manager.SORTED == True
    
    # Taking name case
    case2 = manager.edit_task_name("item1","item2")
    
    tasks_case2 = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    assert tasks_case2 == old_tasks
    assert not case2
    assert manager.MODIFIED_ITEM == False
    assert manager.UP_TO_DATE == True
    assert manager.SORTED == True

    # Success case
    case3 = manager.edit_task_name("item1","some1")
    case3 = manager.edit_task_name("item2","some2")
    case3 = manager.edit_task_name("item3","some3")
    
    tasks_case3 = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    expected = {('some1', False, 1), ('some2', True, 2), ('some3', False, 3)}
    
    assert tasks_case3 == expected
    assert case3

    assert manager.MODIFIED_ITEM == True
    assert manager.UP_TO_DATE == False
    assert manager.SORTED == False

    print("test_edit_task_name passed!")

test_edit_task_name()
print("done testing edit_task_name()")
print()

# Test delete_task()--------------------------

def test_delete_task():

    manager = TaskManager()

    manager.tasks.clear()

    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}
    manager.tasks["item3"]={"done":False,"priority":3}

    old_tasks = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    manager.MODIFIED_ITEM = False
    manager.UP_TO_DATE = True
    manager.SORTED = True

    # Task does not exist case
    case1 = manager.delete_task("some")

    tasks_case1 = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}
    
    assert not case1
    assert old_tasks == tasks_case1

    assert manager.MODIFIED_ITEM == False
    assert manager.UP_TO_DATE == True
    assert manager.SORTED == True

    # Task does not exist case
    case2 = manager.delete_task("item2")

    tasks_case2 = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}
    expected = {('item1', False, 1), ('item3', False, 3)}    

    assert case2
    assert tasks_case2 == expected

    assert manager.MODIFIED_ITEM == True
    assert manager.UP_TO_DATE == False
    assert manager.SORTED == False

    print("test_delete_task passed!")

test_delete_task()
print("done testing delete_task()")
print()

# Test save_tasks() & load_tasks()--------------------------


def test_save_tasks_and_load_tasks ():
    global FILE_NAME
    FILENAME_2 = "test_main_file.txt"

    manager = TaskManager()


    if os.path.exists(FILENAME_2):
        os.remove(FILENAME_2)
    
    manager.tasks.clear()

    FILE_NAME=FILENAME_2
    
    manager.tasks["item1"]={"done":False,"priority":1}
    manager.tasks["item2"]={"done":True,"priority":2}
    manager.tasks["item3"]={"done":False,"priority":3}

    manager.UP_TO_DATE = False

    manager.save_tasks(FILENAME_2)
    assert manager.UP_TO_DATE == True

    manager.tasks.clear()
    manager.UP_TO_DATE = False
    FILE_NAME = "some.txt"

    case1 = manager.load_tasks(FILE_NAME)

    tasks = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}

    assert manager.UP_TO_DATE == False
    assert not case1
    assert not tasks
    
    # Success load case
    manager.tasks.clear()
    manager.UP_TO_DATE = False

    case2 = manager.load_tasks(FILENAME_2)

    tasks = {(task_name,info["done"],info["priority"]) for task_name, info in manager.tasks.items()}
    expected = {('item1', False, 1),('item2', True, 2), ('item3', False, 3)}

    assert manager.UP_TO_DATE == True
    assert case2
    assert tasks == expected
    
    if os.path.exists(FILENAME_2):
        os.remove(FILENAME_2)

    print("test_save_tasks_and_load_tasks passed!")

test_save_tasks_and_load_tasks()
print("done testing save_tasks() and load_tasks()")
print()

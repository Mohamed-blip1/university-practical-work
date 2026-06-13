
// main.c

#include "my_utils.h"

/* #include <stdatomic.h> */
#include <stdbool.h>
#include <stdio.h>
#include <string.h> // strcpy

#define MAX_TASKS 20
#define BUFFER_SIZE 1024

typedef struct
{
  char name[52];
  int done;
  int priority;

} Task;

typedef enum
{
  FAIL,
  N_SUCC, // Failed but error already handled
  SUCC,
  N_SPACE,
  FULL,
  EMPTY,
  N_EXIST,
  TASK_ALREADY_DONE,
  N_SUPP,

} STATUS;

void menu(void);

void check_read_status(const UTILS_STATUS *status);

STATUS get_task_name(char *buffer, size_t buffer_size, size_t task_name_size);
void check_get_task_name_status(const STATUS *status);

STATUS get_task_priority(int *priority);

STATUS add_task(Task *tasks, size_t *tasks_size, size_t tasks_capacity,
                const char *taskname, int *priority);
void check_add_task_status(const STATUS *status);

STATUS list_tasks(const Task *tasks, size_t tasks_size);
void check_list_tasks_status(const STATUS *status);

STATUS mark_task_as_done(Task *tasks, size_t tasks_size, const char *taskname);
void check_mark_task_as_done_status(const STATUS *status);

int main(void)
{
  Task tasks[MAX_TASKS];
  size_t tasks_size = 0;
  size_t tasks_capacity = sizeof(tasks) / sizeof(tasks[0]);

  char buffer[BUFFER_SIZE];
  int choice;
  UTILS_STATUS util_status;
  STATUS status;
  bool exit_flag = false;

  menu();
  while (true)
  {
    choice = 0;
    printf("[4. menu] > ");
    util_status = read_int(&choice);
    if (util_status != UTIL_SUCC)
    {
      check_read_status(&util_status);
      continue;
    }

    switch (choice)
    {

    case 0:
      exit_flag = true;
      break;

    case 1:
    {
      int priority;
      status = get_task_name(buffer, BUFFER_SIZE, sizeof(tasks[0].name));

      if (status != SUCC)
      {
        printf("Error: Could not get task name from user\n");
        check_get_task_name_status(&status);
        continue;
      }

      status = get_task_priority(&priority);
      if (status == FAIL)
      {
        printf("Error: priority is NULL.\n");
        break;
      }
      else if (status != SUCC)
      {
        printf("Warning: unusual Error in get_task_priority().\n");
        break;
      }

      status = add_task(tasks, &tasks_size, tasks_capacity, buffer, &priority);

      if (status != SUCC)
      {
        printf("Error: Could not add task.\n");
        check_add_task_status(&status);
      }
      else
      {
        printf("✓ Task added successfully.\n");
      }
    }
    break;

    case 2:
      status = list_tasks(tasks, tasks_size);

      if (status != SUCC)
      {
        printf("Error: Could not list tasks.\n");
        check_list_tasks_status(&status);
      }
      else
      {
        printf("✓ Tasks listed successfully.\n");
      }

      break;

    case 3:

      status = get_task_name(buffer, BUFFER_SIZE, sizeof(tasks[0].name));

      if (status != SUCC)
      {
        printf("Error: Could not get task name from user.\n");
        check_get_task_name_status(&status);
        continue;
      }

      status = mark_task_as_done(tasks, tasks_size, buffer);

      if (status != SUCC)
      {
        printf("Error: Couldn't mark task as done.\n");
        check_mark_task_as_done_status(&status);
      }
      else
      {
        printf("✓ Task marked as done successfully.\n");
      }

      break;

    case 4:
      menu();
      break;

    default:
      printf("Error: invalide choice.\n");
    }

    if (exit_flag == true)
    {
      printf("Goodbye.\n");
      break;
    }
  }

  return 0;
}

void menu(void)
{
  printf("\n");
  printf("=== Menu ===\n");
  printf("1. Add task\n");
  printf("2. List tasks\n");
  printf("3. Mark task as done\n");
  printf("4. Menu\n");
  printf("0. Exit\n");
  printf("\n");
}

void check_read_status(const UTILS_STATUS *status)
{
  if (status != NULL)
  {
    if (*status != UTIL_SUCC)
    {
      if (*status == UTIL_FAIL)
      {
        printf("Error: buffer is NULL or fgets failed.\n");
      }
      else if (*status == UTIL_TRUNC)
      {
        printf("Error: input is too long.\n");
      }
      else if (*status == UTIL_N_DIGIT)
      {
        printf("Error: input is not a valid digit.\n");
      }
      else if (*status == UTIL_RANGE)
      {
        printf("Error: overflow occurs, number is out of range.\n");
      }
      else
      {
        printf("Error: unusuale error!\n");
      }
    }
    else
    {
      printf("Warning: input was successfully readed.\n");
    }
  }
  else
  {
    printf("Error: status is NULL.\n");
  }
}

STATUS get_task_name(char *buffer, size_t buffer_size, size_t task_name_size)
{
  UTILS_STATUS util_status;
  bool ask_again;

  if (buffer == NULL)
  {
    return FAIL;
  }

  if (buffer_size <= 2 || task_name_size <= 2)
  {
    return N_SPACE;
  }

  do
  {
    ask_again = false;
    printf("Enter task name: ");
    util_status = read_line(buffer, buffer_size);

    if (util_status != UTIL_SUCC)
    {
      check_read_status(&util_status);
      ask_again = true;
    }

#ifdef DUBUG
    printf("buffer size: %zu\n", strlen(buffer));
    printf("task_name_size: %zu\n", task_name_size);
#endif

    if ((strlen(buffer) + 1) > task_name_size)
    {
      // 1 byte for '\0'
      printf("Warning: Please enter a task name less than '%zu' "
             "characters.\n",
             (task_name_size - 1));
      ask_again = true;
    }

  } while (ask_again == true);

  return SUCC;
}

STATUS get_task_priority(int *priority)
{
  UTILS_STATUS util_status;
  bool ask_again = false;

  if (priority == NULL)
  {
    return FAIL;
  }

  do
  {
    ask_again = false;

    printf("Enter task priority (1-3): ");
    util_status = read_int(priority);

    if (util_status != UTIL_SUCC)
    {
      check_read_status(&util_status);
      ask_again = true;
    }

    if (!(*priority >= 1 && *priority <= 3))
    {
      printf("Error: please enter a number between 1 and 3.\n");
      ask_again = true;
    }

  } while (ask_again);

  return SUCC;
}

void check_get_task_name_status(const STATUS *status)
{
  if (status != NULL)
  {
    if (*status != SUCC)
    {
      if (*status == FAIL)
      {
        printf("Error: buffer is NULL.\n");
      }
      else if (*status == N_SPACE)
      {
        printf("Error: The buffer or task name does not have enough size.\n");
      }
      else
      {
        printf("Error: Unusual error.\n");
      }
    }
    else
    {
      printf("Warning: The task name was entered successfully.\n");
    }
  }
  else
  {
    printf("Error: status is NULL.\n");
  }
}

STATUS add_task(Task *tasks, size_t *tasks_size, size_t tasks_capacity,
                const char *taskname, int *priority)
{
  if (tasks == NULL || tasks_size == NULL || taskname == NULL ||
      priority == NULL)
  {
    return FAIL;
  }

  if (*tasks_size >= tasks_capacity)
  {
    return FULL;
  }

  // '1' Byte for '\0'
  if (sizeof(tasks[0].name) < (strlen(taskname) + 1))
  {
    return N_SPACE;
  }

  if (!(*priority >= 1 && *priority <= 3))
  {
    return N_SUPP;
  }

  strcpy(tasks[*tasks_size].name, taskname);

  tasks[*tasks_size].done = false;

  tasks[*tasks_size].priority = *priority;

  (*tasks_size)++;

  return SUCC;
}

void check_add_task_status(const STATUS *status)
{
  if (status != NULL)
  {
    if (*status != SUCC)
    {
      if (*status == FAIL)
      {
        printf("Error: Tasks or tasks_size or taskname or priority is NULL.\n");
      }
      else if (*status == N_SUPP)
      {
        printf("Error: priority level is not supported.\n");
      }
      else if (*status == FULL)
      {
        printf("Error: Tasks are full, please delete some tasks.\n");
      }
      else if (*status == N_SPACE)
      {
        printf(
            "Error: The provided task name size is larger than the task name "
            "size\n");
      }
      else
      {
        printf("Error: Unusual error.\n");
      }
    }
    else
    {
      printf("Warning: Task was added successfully.\n");
    }
  }
  else
  {
    printf("Error: status is NULL.\n");
  }
}

STATUS list_tasks(const Task *tasks, size_t tasks_size)
{
  size_t i;

  if (tasks == NULL)
  {
    return FAIL;
  }

  if (tasks_size == 0)
  {
    return EMPTY;
  }

  printf("\n==== Tasks ====\n");

  for (i = 0; i < tasks_size; i++)
  {
    if (tasks[i].done == true)
    {
      printf("[x] %s\n", tasks[i].name);
    }
    else
    {
      printf("[ ] %s\n", tasks[i].name);
    }
  }

  printf("\n");

  return SUCC;
}

void check_list_tasks_status(const STATUS *status)
{
  if (status != NULL)
  {
    if (*status != SUCC)
    {
      if (*status == FAIL)
      {
        printf("Error: Tasks is NULL.\n");
      }
      else if (*status == EMPTY)
      {
        printf("Error: No tasks yet.\n");
      }
      else
      {
        printf("Error: Unusual error.\n");
      }
    }
    else
    {
      printf("Warning: Tasks was listed successfully.\n");
    }
  }
  else
  {
    printf("Error: status is NULL.\n");
  }
}

STATUS mark_task_as_done(Task *tasks, size_t tasks_size, const char *taskname)
{
  size_t i;

  if (tasks == NULL || taskname == NULL)
  {
    return FAIL;
  }

  if (tasks_size == 0)
  {
    return EMPTY;
  }

  for (i = 0; i < tasks_size; i++)
  {
    if (strcmp(tasks[i].name, taskname) != 0)
    {
      continue;
    }
    if (tasks[i].done != true)
    {
      tasks[i].done = true;
      return SUCC;
    }
    return TASK_ALREADY_DONE;
  }

  return N_EXIST;
}

void check_mark_task_as_done_status(const STATUS *status)
{
  if (status != NULL)
  {
    if (*status != SUCC)
    {
      if (*status == FAIL)
      {
        printf("Error: Tasks or taskname is NULL.\n");
      }
      else if (*status == EMPTY)
      {
        printf("Error: No tasks yet.\n");
      }
      else if (*status == TASK_ALREADY_DONE)
      {
        printf("Warning: Task already done.\n");
      }
      else if (*status == N_EXIST)
      {
        printf("Error: Task does not exist.\n");
      }
      else
      {
        printf("Error: Unusual error.\n");
      }
    }
    else
    {
      printf("Warning: Task was marked as done successfully.\n");
    }
  }
  else
  {
    printf("Error: status is NULL.\n");
  }
}

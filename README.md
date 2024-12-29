# Python-basic-task-manager-application-

# Summary.

•	"In this simple Task Manager project, I created a Python application that allows users to manage tasks. I used lists to store multiple tasks, and dictionaries to store task details such as description and completion status. The program allows users to add tasks, mark them as completed, and delete them. However, this version does not use file I/O, so tasks are only stored in memory and will be lost when the program is closed."

# Step by step explaination of project.
"The Task Manager project is a command-line Python application that allows users to manage and organize their tasks. Users can add tasks, view them, mark them as completed, and delete them. This project helps demonstrate my understanding of basic data structures like lists and dictionaries, as well as how to build a simple interactive program using Python."

2. Project design and class sturucture.
"The core of the project is the TaskManager class. This class has methods for managing tasks and their statuses. I chose to use a class because it helps encapsulate the task-related operations and makes the code more organized and reusable. The class has an attribute called tasks, which is a list where I store all the tasks."


3. Walk-in through class methods.
add_task(description)
"The add_task method takes a task description as input and creates a dictionary representing the task. Each dictionary has two keys: 'description', which stores the task's name, and 'completed', which stores whether the task has been completed (initially set to False). This dictionary is then appended to the tasks list."

view_tasks()
"The view_tasks method iterates through the tasks list and displays each task along with its completion status. If a task is completed, it prints 'Completed', otherwise, it prints 'Not Completed'. This allows the user to see all tasks and their current status."

mark_task_completed(task_number)
"The mark_task_completed method allows the user to mark a task as completed. It accepts a task number as input, checks if the task exists in the tasks list, and updates its 'completed' status to True. If the task number is invalid, an error message is shown."

delete_task(task_number)
"The delete_task method removes a task from the list based on the task number provided by the user. It uses the pop() method to remove the task from the list and provides a success message. If the task number is invalid, an error message is displayed."


4. Explaination of main function.
"The main function provides a simple command-line interface (CLI) to interact with the program. It displays a menu with options to add tasks, view tasks, mark tasks as completed, or delete tasks. The user can input their choice, and based on that input, the corresponding method in the TaskManager class is called."
"For instance, if the user selects 'Add Task', the program prompts them for a task description, which is then passed to the add_task method to be added to the list. Similarly, the other options call the appropriate methods to view, update, or delete tasks."

5. How the program will work.
"Here’s how the program works in practice. When the user starts the program, it shows a menu with options. If they choose '1', they can add a task by typing a description. The task is then stored in the list as a dictionary. The user can view all tasks by selecting '2', and the program will show each task's description and completion status. If they choose '3', they can mark a task as completed by entering the task number, and if they choose '4', they can delete a task. Finally, if they choose '5', the program will exit."
"For example, if a user adds a task called 'Learn Python', the task is added to the list. If they mark it as completed, the status for that task will change to 'Completed'."


# Data Structures:

1. How Lists are Used:
o	In your project, tasks are stored in a list. Each task can be represented as a dictionary, with the task's description and completion status being key-value pairs in the dictionary.
o	The list is used to keep all tasks together, and each task is an individual dictionary inside this list.

2. How Dictionaries are Used:
o	Each task in the list is stored as a dictionary, where:
	"description" (a string) is the key representing the task’s description (e.g., "Learn Python").
	"completed" (a boolean: True or False) is the key representing whether the task has been completed or not.

   
# Explaination of code.

1.	Class Definition (TaskManager):
o	The class contains a list called tasks that stores all the tasks, where each task is represented by a dictionary.
o	Each dictionary stores a task's description and its completion status (completed is a boolean).

2.	Methods in the TaskManager Class:
o	add_task(description): Adds a new task to the tasks list.
o	view_tasks(): Displays all tasks along with their completion status.
o	mark_task_completed(task_number): Marks a task as completed based on the task number provided.
o	delete_task(task_number): Deletes a task by its task number.

3.	Main Function:
o	Provides a simple menu to allow the user to choose an option.
o	Users can add tasks, view tasks, mark tasks as completed, delete tasks, or exit the program.


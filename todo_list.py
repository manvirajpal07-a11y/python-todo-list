## To-Do List 

## Initialize a empty list to store tasks

tasks = []

## Function to add task
def add_task():
    task = input("Enter a new task : ")
    tasks.append(task)  ##add the task to the list
    print(f"Task '{task}' added.")
    
    

##Function to view all tasks
def view_tasks():
    if not tasks:
        print("Your to-do list is empty")
    else:
        print("Your tasks")
        for index, task in  enumerate(tasks,start=1):
            print(f"{index}.{task}")
            
            
            
## Function to delete task
def delete_task():
    view_tasks()  ## show the user the list first
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0<task_num<=len(tasks):
            removed_task = tasks.pop(task_num-1) ## Remove the task by index
            print(f"Task '{removed_task}' deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
        
        
## Function to display the menu
def menu():
    print("\nTo-Do List Menu: ")
    print("1. Add a new task ")
    print("2. View all tasks ")
    print("3. Delete a task ")
    print("4. Exit")
    
    
    
## Main function to run To-Do list application
def run_todo_list():
    while True:
        menu()   ## Show the menu
        choice=input("Enter your choice (1-4): ")
        if choice == '1' :
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the To-Do list Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4)")
            
    
## Run the to-do list application 
run_todo_list()
            
              
        
    



















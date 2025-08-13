todo_list = []
def add_task(task):
    todo_list.append(task)
    
def remove_task(task):
    todo_list.remove(task)
    
def modify_task():
    modify = int(input("what is the index number of the task you want to change: "))
    new = input("what do you want to change it to: ")
    todo_list[modify] = new
    
def display_tasks():
    print(f"You still have to {todo_list}")
    
while True:
    print("\n1. Add Task\n2. Remove Task\n3. Modify task\n4. View Tasks\n5. Exit")
    choice = input("Enter choice : ")
    
    if choice == "1":
        add = input("what task do you want to add: ")
        add_task(add)
        print(f"{add} has been added to your list")
        
    elif choice == "2":
        remove = input("What task do you want to remove from your list: ")
        remove_task(remove)
        print(f"{remove} has been removed from your list")
        
    elif choice == "3":
        modify_task()
        print(f"You have changed the task")
        
    elif choice == "4":
        display_tasks()
        
    elif choice == "5":
        print("You have exited the program")
        break
    
    else:
        print("That is not one of the options")
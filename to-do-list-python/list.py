# Function to manage to-do-list
def task():
    tasks = [] #empty list
    print("----WELCOME TO YOUR TO DO LIST.----")

    #Take input from user
    try:
        totaltask = int(input("Enter how many task you need to complete: "))

    # Handle keyboard interruption
    except KeyboardInterrupt:
        print("Program interrupted.")
        return

    #Loop to append task in list
    for i in range(1, totaltask + 1):
        taskname = input(f"Enter task {i}: ")
        tasks.append(taskname)

    print(f"you need to do this tasks \n {tasks}")

    #Ask user to choose
    while True:
        operation = int(input("Enter your choice \nchoice no - 1: add \nchoice no - 2: update \nchoice no - 3: delete \nchoice no - 4: view \nchoice no - 5: exit\n"))
        # Add new task
        if operation == 1:
            print(f"you tasks are {tasks}")
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"task {add} has been added to your list.")

        # Update existing task
        elif operation == 2:
            update = input("Enter task you want to update: ")
            if update in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"updated task{up}")

        # Delete existing task
        elif operation == 3:
            delete = input("which task do you want to delete: ")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"Task {delete} has been deleted.")

        # View list
        elif operation == 4:
            print(f"you tasks are {tasks}")

        # Exist program
        elif operation == 5:
            print("Thank you, have a nice day.")
            break

        # Handle invalid choice
        else:
            print("Please enter a valid choice.")

# Call function
task()        
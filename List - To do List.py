#create an empty to do list

todo_list = []

while True:
    print('\n*** WELCOME TO MY TO DO APP ***\n')
    print('Here are your uncompleted task:\n')
    for index, value in enumerate (todo_list, start = 1):
        print(f'{index}, {value}')
    
    # get user choice
    choice = input('\nWhat do you want to do? (add, edit, delete, complete, quit): ').lower()

    # check for user choice and perform necessary operation
    if choice == 'quit':
        print('Thank you for using my todo app. Goodbye!')
        break
    elif choice == "add":
        task = input("Enter a task: ").lower()
        # add user task to the list   
        todo_list.append(task)
    elif choice == 'complete':
        index = int(input("Enter the index of the task you want to complete: "))
        # check if index is valid
        if index > len(todo_list):
        print('Invalid Index! Please enter a valid index.')
        # check for -ve or 0 index
    elif index <= 0:
        print('Invalid Index! Please enter a valid Index')
        # add user task to the list
        todo_list.append(task)
        # check for valid index and complete task
    elif 1 <= index <= len(todo_list):
        todo_list.pop(index - 1)
    
    
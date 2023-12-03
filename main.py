from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below: ")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    # Depending on the option the user chooses, it will go into th if statement and do the corresponding action.
    if user_action.startswith('add'):
        # You have to type 'add' follow by the todo, ex: 'add Study Python'.
        # we will store in a variable 'todo' the user input, parting from index 4 of the string inputted,
        #  leaving 'add ' out.
        todo = user_action[4:]

        # we call the function get_todos(), which will return the content inside the 'todos.txt' file
        # The content will be stored in the variable 'todos' as a list.
        todos = get_todos()

        # Since we have a list in 'todos' we append the 'todo' entered by the user.
        todos.append(todo + '\n')

        # Now we just call the 'write_todos()' function and write the content with the updated list
        write_todos(todos)

    elif user_action.startswith('show'):
        # Call the get_todos() function to get the list of existing to-dos
        todos = get_todos()

        # We loop over them to display them in sequence using the enumerate function.
        for index, item in enumerate(todos):
            # We strip the break line for each todo, since they already have a break line, this will prevent
            #  having to break lines.
            item = item.strip('\n')
            print(f"{index + 1}. {item}")
    elif user_action.startswith('edit'):
        # 'edit' will accept the word edit followed by the number of todo, it's not like add, where the user enters
        # 'add Learn Pyton'
        # That's why we put a try-except, to prevent the user from doing that.
        try:
            # We take the input only from index 5 onwards, since it's going to be a number, we convert it to an int.
            number = int(user_action[5:])

            # we call the function get_todos(), which will return the content inside the 'todos.txt' file
            # The content will be stored in the variable 'todos' as a list.
            todos = get_todos()

            # We replace the existing to-do in the list by its index with a new todo by tue user.
            todos[number - 1] = input("Enter new todo: ") + '\n'

            # Now we just call the 'write_todos()' function and write the content with the updated list
            write_todos(todos)
        except ValueError:
            # In case the user doesn't input the right format, this message pops up.
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        # Use a try-except in case the user wants to complete a todo that's out of range.
        try:
            # We take the input only from index 9 onwards, since it's going to be a number, we convert it to an int.
            number = int(user_action[9:])

            # we call the function get_todos(), which will return the content inside the 'todos.txt' file
            # The content will be stored in the variable 'todos' as a list.
            todos = get_todos()

            # We make a variable we the index of the complete to-do by the user is stored
            index = number - 1
            # We save the removed to-do in a variable, while striping a break line from it, so when its printed it
            # doesn't have a break line in the output.
            removed_todo = todos[index].strip('\n')
            # We just delete the todo with the corresponding index
            todos.pop(index)

            # Now we just call the 'write_todos()' function and write the content with the updated list
            write_todos(todos)

            # we show the user what to-do was removed
            message = f"To-Do '{removed_todo}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        # Exits the program, breaking the while loop.
        break
    else:
        # Just in case the user enters an invalid option
        print("Command is not valid.")
print("Bye!")

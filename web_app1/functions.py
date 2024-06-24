FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ It read a file and return a
    list of to-dos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ It reads a list and write to-dos in a file """
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_local)


# print(__name__)
# print(type(__name__))

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
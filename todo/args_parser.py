import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="operation",help="Available todo operations")

    subparser.add_parser("create", help="create new todo")
    #parser_create.add_argument("-p", "--path", help=f"Optional path for the todo file. Default is current directory/")

    subparser.add_parser("read", help="read todo tasks")

    parser_add_task = subparser.add_parser("add", help="add task to todo")
    parser_add_task.add_argument("task", help="a quoted message to add to todo")
    parser_add_task.add_argument("--prio", type=int, help="set the task priority")

    parser_remove_task = subparser.add_parser("remove", help="remove task from todo")
    parser_remove_task.add_argument("taskID", help="ID of task to be removed")

    parser_update_task = subparser.add_parser("update", help="update task, see -h for arguments")
    parser_update_task.add_argument("taskID", type=int, help="id of the task being updated")
    parser_update_task.add_argument("--cont", help="new content")
    parser_update_task.add_argument("--prio", type=int, help="new priority")

    subparser.add_parser("config", help="opens the config file")

    parser_set_todo = subparser.add_parser("set", help="set the todo file to be used")
    parser_set_todo.add_argument("todoDir", help="directory of the todo file, can use . to mean current directory")


    subparser.add_parser("interact")

    subparser.add_parser("reset_ids", help="reset the IDs")

    args = parser.parse_args()
    
    return args
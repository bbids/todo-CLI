import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="operation",help="Available To-Do operations")

    subparser.add_parser("create", help="create new To-Do.")
    #parser_create.add_argument("-p", "--path", help=f"Optional path for the todo file. Default is current directory/")

    subparser.add_parser("read", help="read To-Do tasks")

    parser_add_task = subparser.add_parser("add", help="add task to To-Do")
    parser_add_task.add_argument("task", help="a quoted message to add to To-Do")
    parser_add_task.add_argument("--prio", type=int, help="set the task priority")

    parser_remove_task = subparser.add_parser("remove", help="remove task from To-Do")
    parser_remove_task.add_argument("taskID", help="A task ID, available in operation read")

    parser_update_task = subparser.add_parser("update", help="update task, see -h for arguments")
    parser_update_task.add_argument("taskID", type=int, help="id of the task being updated")
    parser_update_task.add_argument("--cont", help="new content")
    parser_update_task.add_argument("--prio", type=int, help="new priority")

    subparser.add_parser("config", help="opens the config file")


    subparser.add_parser("interact")

    subparser.add_parser("reset_ids", help="reset the IDs")

    args = parser.parse_args()
    
    return args
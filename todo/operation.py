import os
import logging
import json
import textwrap

class Operation:
    """Namespace for available operations"""

    def display_tasks_interactive(i = 0):
        """Display the tasks in a pretty way."""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)
        width = 37

        i = 0 if i < 0 else i
        i = min(i, len(data[TodoKeys.KEY_TASKS]) - 1)
        for ind, task in enumerate(data[TodoKeys.KEY_TASKS]):
            id = task[TaskKeys.KEY_ID]
            priority = task[TaskKeys.KEY_PRIORITY]
            content = task[TaskKeys.KEY_CONTENT]

            match priority:
                case 5:
                    priorityColor = Colors.LIGHT_GRAY
                    priority = "Optional  "
                case 4:
                    priorityColor = Colors.LIGHT_BLUE
                    priority = "Non-urgent"
                case 3:
                    priorityColor = Colors.YELLOW
                    priority = "Necessary "
                case 2:
                    priorityColor = Colors.PURPLE
                    priority = "Important "
                case 1:
                    priorityColor = Colors.RED
                    priority = "Critical  "
                case _:
                    priorityColor = Colors.RED
                    priority = "Other     "

            VERTICAL_LINE = f"{priorityColor}\u2502{Colors.DEFAULT}"

            # change the corner of a box, when the box is beeing selected
            if len(data[TodoKeys.KEY_TASKS]) - i - 1== ind:
                topLeft = Colors.OKGREEN + "\u231C" + priorityColor
                topRight = Colors.OKGREEN + "\u231D" + priorityColor
                botLeft = Colors.OKGREEN + "\u231E" + priorityColor
                botRight = Colors.OKGREEN + "\u231F" + priorityColor
            else:
                topLeft = " "
                topRight = ""
                botLeft = " "
                botRight = ""

            # draw a box containing content with border color based on priority level
            print(f"{Colors.DEFAULT}Id:", id, f"\n{priorityColor}\u25BC{Colors.DEFAULT}" 
                  f" Priority:{priorityColor}", priority)
            print(priorityColor + topLeft + "_"*(width) + topRight)
            wrapped = textwrap.wrap(content, width = 35)
            result = f'{VERTICAL_LINE}\n{VERTICAL_LINE}'.join(line.ljust(width) for line in wrapped)
            result += f"{VERTICAL_LINE}".ljust(width)
            print(VERTICAL_LINE + result)
            print(priorityColor + botLeft + "‾"*(width) + botRight + Colors.DEFAULT)

            if len(data[TodoKeys.KEY_TASKS]) - i == ind:
                break



        """
        # template of a box
        boxColor = Colors.DEFAULT + Colors.BOLD
        print(boxColor + '\u231C' + "_"*(width - 2) + '\u231D')
        wrapped = textwrap.wrap("Content", width = 35)
        result = f'{VERTICAL_LINE_UTF}\n{VERTICAL_LINE_UTF}'.join(line.ljust(35) for line in wrapped)
        result += f"{VERTICAL_LINE_UTF}".ljust(35)
        print(VERTICAL_LINE_UTF + result)
        print(boxColor + '\u231E' + "‾"*(width - 2) + '\u231F')
        """

        # we return i, to prevent overflow
        return i
        
    def display_tasks():
        """Display the tasks in a pretty way."""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)
        width = 35

        for task in data[TodoKeys.KEY_TASKS]:
            id = task[TaskKeys.KEY_ID]
            priority = task[TaskKeys.KEY_PRIORITY]
            content = task[TaskKeys.KEY_CONTENT]

            match priority:
                case 5:
                    priorityColor = Colors.LIGHT_GRAY
                    priority = "Optional  "
                case 4:
                    priorityColor = Colors.LIGHT_BLUE
                    priority = "Non-urgent"
                case 3:
                    priorityColor = Colors.YELLOW
                    priority = "Necessary "
                case 2:
                    priorityColor = Colors.PURPLE
                    priority = "Important "
                case 1:
                    priorityColor = Colors.RED
                    priority = "Critical  "
                case _:
                    priorityColor = Colors.RED
                    priority = "Other     "

            VERTICAL_LINE = f"{priorityColor}\u2502{Colors.DEFAULT}"

            # draw a box containing content with border color based on priority level
            print(f"{Colors.DEFAULT}Id:", id, f"\n{priorityColor}\u25BC{Colors.DEFAULT}" 
                  f" Priority:{priorityColor}", priority)
            print(priorityColor + " " + "_"*(width))
            wrapped = textwrap.wrap(content, width = 35)
            result = f'{VERTICAL_LINE}\n{VERTICAL_LINE}'.join(line.ljust(width) for line in wrapped)
            result += f"{VERTICAL_LINE}".ljust(width)
            print(VERTICAL_LINE + result)
            print(priorityColor + " " + "‾"*(width) + Colors.DEFAULT)


    def remove_task_interactive(i):
        """Remove the task currently beeing selected. Used in interactive mode. """
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)
        tasks = data[TodoKeys.KEY_TASKS]

        ind_to_delete = len(data[TodoKeys.KEY_TASKS]) - i - 1
        data[TodoKeys.KEY_TASKS] = [item for ind, item in enumerate(tasks) if ind != ind_to_delete]

        with open(todo_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def reset_ids():
        """Reset the task IDs"""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)

        id = 0
        for item in data[TodoKeys.KEY_TASKS]:
            item[TaskKeys.KEY_ID] = id
            id += 1
        
        with open(todo_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)





if __name__ == "__main__":
    Operation.remove_single_task(1)
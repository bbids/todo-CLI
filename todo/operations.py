import textwrap

from todo.constants import Colors

def display_tasks(tasks):
        """Display the tasks in a pretty way."""
        width = 35

        for item in tasks:
            id = item[0]
            content = item[1]
            priority = item[2]

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
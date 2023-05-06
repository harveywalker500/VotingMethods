import sys


def init():
    """Initializes the program and sets the logger."""
    print("""
---------------
VotingMethods
Written by:
Harvey Walker
---------------""")
    return "ERROR"


def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        menu = str(input("VM> "))
        menu = menu.split(" ")
        match menu[0]:
            case "help":
                try:
                    help_menu(menu[1])
                except IndexError:
                    help_menu("help")
            case "exit":
                sys.exit(0)
            case "logging":
                logging_menu(menu)
            case _:
                print("Invalid command. Type 'help' for a list of commands.")


def logging_menu(menu):
    """Handles changing the logging level."""
    if menu[1] == "critical":
        print("Logging level set to CRITICAL.")
        return "CRITICAL"
    elif menu[1] == "error":
        print("Logging level set to ERROR.")
        return "ERROR"
    elif menu[1] == "warning":
        print("Logging level set to WARNING.")
        return "WARNING"
    elif menu[1] == "info":
        print("Logging level set to INFO.")
        return "INFO"
    elif menu[1] == "debug":
        print("Logging level set to DEBUG.")
        return "DEBUG"
    elif menu[1] == "notset":
        print("Logging level set to NOTSET.")
        return "NOTSET"
    else:
        print("Invalid logging level.")

    print("NOTE: This feature is not yet implemented.")


def help_menu(command):
    """Displays the help menu."""
    match command:
        case "help":
            print("""Available commands:
logging [level] - Sets the logging level
help [command] - Displays help for a command
exit - Exits the program""")

        case "exit":
            print("exit - Exits the program")

        case "logging":
            print("""logging [level] - Sets the logging level
    Available levels:
        critical
        error
        warning
        info
        debug
        notset""")

        case _:
            print("No help available for this command, or command is not available.")

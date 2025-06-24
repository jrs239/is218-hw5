import os
import importlib
from decimal import Decimal, InvalidOperation

COMMANDS = {}

def load_commands():
    command_folder = "commands"
    for filename in os.listdir(command_folder):
        if filename.endwith(".py") and not filename.startswith("__"):
            module_name = f"{command_folder}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and hasattr(obj, "execute"):
                    instance = obj()
                    COMMANDS[instance.name] = instance

def repl():
    print("Welcome to the Calculator App!")
    print("Type 'menu' to view commands or 'exit' to quit.\n")

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "menu":
            print("Available commands:", ", ".join(COMMANDS.keys()))
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Usage: <operation> <num1> <num2>")
            continue

        operation, a_str, b_str = parts

        try:
            a = Decimal(a_str)
            b = Decimal(b_str)
        except InvalidOperation:
            print(f"Invalid input: '{a_str}' or '{b_str}' is not a number.")
            continue

        if operation in COMMANDS:
            try:
                result = COMMANDS[operation].execute(a, b)
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Division by zero.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Unknown command: '{operation}'. Type 'menu' to see available options.")

if __name__ == "__main__":
    load_commands()
    repl()

"""
Task_7.py.

Created by: Arkin E
Date: 26.02.2024
"""

def input_int(prompt) -> int:
    """
    Prompts the user for an integer, validates the input, and returns it.

    Args:
    ----
    prompt: The message to display to the user.

    Returns:
    -------
    The integer entered by the user.
    """

    loop = True
    while loop:
        try:
            value = int(input(prompt))
            loop = False
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return value

def input_float(prompt) -> float:
    """
    Prompts the user for a float number, validates the input, and returns it.

    Args:
    ----
    prompt: The message to display to the user.

    Returns:
    -------
    The floating-point number entered by the user.
    """
    loop = True
    while loop:
        try:
            value = float(input(prompt))
            loop = False
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    return value

def input_bool(prompt) -> bool:
    """
    Prompts the user for a boolean value (yes/no).
    
    validates the input, and returns it

    Args:
    ----
    prompt: The message to display to the user.

    Returns:
    -------
    The boolean value entered by the user
    (True for yes/y/true/t, False for no/n/false/f).
    """

    valid_inputs = ["yes", "y", "true", "t", "no", "n", "false", "f"]

    loop = True
    while loop:
        value = input(prompt).lower()
        if value in valid_inputs:
            return True
            loop = False
        else:
            print("Invalid input. Please enter yes/no or true/false.")

    return value in {"yes", "y", "true", "t"}

age = input_int("How old are you? ")
is_happy = input_bool("Are you happy? ")
average_
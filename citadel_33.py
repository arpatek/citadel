#!/usr/bin/env python3

"""
citadel_33.py - Secure Pattern-Based Password Generator
========================================================

Citadel-33 generates strong, human-readable passwords using customizable
patterns, optional scope tagging, and randomized entropy. Useful for devs,
sysadmins, and anyone who wants structured but secure passwords.

Author: Juan J Garcia (@0xjuang)

Dependencies:
-------------
- Python 3.6+
- Standard library only: random, string

Sample Usage:
-------------
$ ./citadel_33.py
"""

# ──[ Standard Library Imports ]─────────────────────────────────────────────
import random
import string
import time

__version__ = "0.1.0"

HEADER_BANNER = """
┌──────────────────────────────────────────────────────────────┐
│                        Citadel-33                            │
│             Pattern-Based Password Generator                 │
│                                                              │
│      Author: Juan J Garcia (0x1G)                            │
│      Description: Generates secure passwords using           │
│                   patterns, scopes, and randomized entropy.  │
└──────────────────────────────────────────────────────────────┘
"""

# ──[ Character Sets Used for Password Generation ]──────────────────────────────
CHAR_LIST = string.ascii_letters
INT_LIST = string.digits
SPECIAL_CHAR_LIST = string.punctuation
FULL_LIST = INT_LIST + CHAR_LIST + SPECIAL_CHAR_LIST


# ──[ User Input & Selection Logic ]────────────────────────────────────────────
def get_usr_info() -> tuple[int, str, str]:
    """
    Prompt the user to choose a password generation style and collect
    pattern and scope inputs if applicable.

    Returns:
        tuple: (passwd_style (int), usr_pattern (str), scope (str))
    """
    # Prompt user until a valid password style is chosen (1, 2, or 3)
    while True:
        try:
            print(
                """
    Choose a password style:

    [1] Random
        ➤ Example: w3#9Tf8z@L

    [2] Pattern + Random
        ➤ Example: myPattern.-r@nd0m!

    [3] Pattern + Scope + Random
        ➤ Example: myPattern.-github.r@nd0m!
    """
            )
            passwd_style = int(input("> ").strip())
            if passwd_style not in [1, 2, 3]:
                print("Invalid option. Please choose 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")

    usr_pattern = ""
    scope = ""

    # If user selects style 2 or 3, collect pattern input
    if passwd_style in [2, 3]:
        usr_pattern = input("Input your desired pattern: ").strip()
        if passwd_style == 3:
            scope = input("What is the scope? (e.g. git, insta, gmail): ").strip()

    return passwd_style, usr_pattern, scope


# ──[ Random Pattern Generator ]────────────────────────────────────────────────
def random_pattern(length: int) -> str:
    """
    Generate a random string of characters with specified length.

    Args:
        length (int): The number of characters to generate.

    Returns:
        str: A randomized string composed of letters, digits, and symbols.
    """
    # Generate a random character list from FULL_LIST
    result: list[str] = []
    for _ in range(int(length)):
        char = random.choice(FULL_LIST)
        result.append(char)
    return "".join(result)


# ──[ Main Execution Flow ]─────────────────────────────────────────────────────
def main() -> None:
    """
    Main execution flow. Handles user input, random generation,
    and password formatting based on chosen style.
    """
    print(HEADER_BANNER)
    time.sleep(2)
    passwd_style, usr_pattern, scope = get_usr_info()

    # Handle style 1: Fully random password
    if passwd_style == 1:
        while True:
            try:
                rand_length = int(
                    input("Choose a password length (>= 10 characters): ").strip()
                )
                if rand_length < 10:
                    print("Password must be at least 10 characters long.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        rand = random_pattern(rand_length)
        password = rand
    # Handle style 2: Pattern + Random
    elif passwd_style == 2:
        while True:
            try:
                rand_length = int(input("Desired length for the random portion: ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")
        rand = random_pattern(rand_length)
        password = f"{usr_pattern}.-{rand}!"
    # Handle style 3: Pattern + Scope + Random
    elif passwd_style == 3:
        while True:
            try:
                rand_length = int(input("Desired length for the random portion: ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")
        rand = random_pattern(rand_length)
        password = f"{usr_pattern}.-{scope}.{rand}!"
    else:
        print("Invalid option.")
        return

    # Print the final generated password
    print(f"\nGenerated Password:\n{password}")


# ──[ Script Entry Point ]──────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

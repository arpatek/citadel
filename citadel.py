#!/usr/bin/env python3
"""
citadel.py - Secure Pattern-Based Password Generator
========================================================================================

Citadel generates strong, human-readable passwords using customizable patterns,
optional scope tagging, and cryptographically secure entropy. Useful for devs,
sysadmins, and anyone who wants structured but secure passwords.

Author: Juan Garcia (arpatek)

Dependencies:
-------------
- Python 3.6+
- Standard library only: secrets, string

Sample Usage:
-------------
$ ./citadel.py
"""

__version__ = "0.2.0"

# ──[ Standard Library Imports ]────────────────────────────────────────────────────────
import secrets
import string
import time


# ──[ Constants ]───────────────────────────────────────────────────────────────────────
HEADER_BANNER = """
┌──────────────────────────────────────────────────────────────┐
│                          Citadel                             │
│             Pattern-Based Password Generator                 │
│                                                              │
│      Author: Juan Garcia (arpatek)                           │
│      Description: Generates secure passwords using           │
│                   patterns, scopes, and randomized entropy.  │
└──────────────────────────────────────────────────────────────┘
"""

CHAR_LIST         = string.ascii_letters
INT_LIST          = string.digits
SPECIAL_CHAR_LIST = string.punctuation
FULL_LIST         = INT_LIST + CHAR_LIST + SPECIAL_CHAR_LIST


# ──[ Input ]───────────────────────────────────────────────────────────────────────────
def get_usr_info() -> tuple[int, str, str]:
    """Prompt the user to choose a password style and collect pattern/scope inputs.

    Returns:
        tuple: (passwd_style (int), usr_pattern (str), scope (str))
    """
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
    scope       = ""

    if passwd_style in [2, 3]:
        usr_pattern = input("Input your desired pattern: ").strip()
        if passwd_style == 3:
            scope = input("What is the scope? (e.g. git, insta, gmail): ").strip()

    return passwd_style, usr_pattern, scope


# ──[ Generator ]───────────────────────────────────────────────────────────────────────
def random_pattern(length: int) -> str:
    """Generate a cryptographically random string of the given length.

    Args:
        length (int): Number of characters to generate.

    Returns:
        str: Random string composed of letters, digits, and symbols.
    """
    return "".join(secrets.choice(FULL_LIST) for _ in range(int(length)))


# ──[ Main ]────────────────────────────────────────────────────────────────────────────
def main() -> None:
    """Run the interactive password generation flow."""
    print(HEADER_BANNER)
    time.sleep(2)
    passwd_style, usr_pattern, scope = get_usr_info()

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
        password = random_pattern(rand_length)

    elif passwd_style == 2:
        while True:
            try:
                rand_length = int(
                    input("Desired length for the random portion: ").strip()
                )
                break
            except ValueError:
                print("Please enter a valid number.")
        password = f"{usr_pattern}.-{random_pattern(rand_length)}!"

    elif passwd_style == 3:
        while True:
            try:
                rand_length = int(
                    input("Desired length for the random portion: ").strip()
                )
                break
            except ValueError:
                print("Please enter a valid number.")
        password = f"{usr_pattern}.-{scope}.{random_pattern(rand_length)}!"

    else:
        print("Invalid option.")
        return

    print(f"\nGenerated Password:\n{password}")


# ──[ Entry Point ]─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

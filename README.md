# Citadel-33

```
┌──────────────────────────────────────────────────────────────┐
│                        Citadel-33                            │
│             Pattern-Based Password Generator                 │
│                                                              │
│      Author: Juan J Garcia (0x1G)                            │
│      Description: Generates secure passwords using           │
│                   patterns, scopes, and randomized entropy.  │
└──────────────────────────────────────────────────────────────┘
```

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Python](https://img.shields.io/badge/python-3.6%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

**Citadel-33** is a pattern-based password generator written in Python. It allows users to generate passwords with optional user-defined patterns and scope tags, ensuring both structure and strong entropy for secure credentials. It is built for terminal-native workflows and serves developers, sysadmins, and power users who want structured password control without compromising randomness.

## Features

- Fully random password generation
- Structured passwords with pattern and scope options
- User-friendly terminal prompts
- Built-in input validation
- Extensible and documented codebase

## Example Styles

```
[1] Random
    ➤ Example: w3#9Tf8z@L

[2] Pattern + Random
    ➤ Example: myPattern.-r@nd0m!

[3] Pattern + Scope + Random
    ➤ Example: myPattern.-github.-r@nd0m!
```

## Usage

```bash
python3 citadel_33.py
```

Follow the prompts to choose your password style, length, and optional pattern/scope.

## Requirements

- Python 3.6 or higher
- No external dependencies (standard library only)

## Roadmap

- [ ] Add CLI flag support via argparse
- [ ] Implement clipboard copy with secure timeout using pyperclip
- [ ] Harden input validation with full try/except coverage
- [ ] Add optional terminal UI (TUI) mode using Textual or npyscreen
- [ ] Export as a pip-installable CLI package

## Author

Juan J. Garcia ([@0xjuang](https://github.com/0xjuang))  

## License

This project is licensed under the MIT License.
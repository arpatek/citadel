



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

**Citadel-33** is a pattern-based password generator written in Python. It allows users to generate passwords with optional user-defined patterns and scope tags, ensuring both structure and entropy for strong credentials. Designed to be terminal-native, it serves developers, sysadmins, and power users who want control over password structure without sacrificing randomness.

## Features

- Pattern + scope based password generation
- Fully random password option
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
python3 citadel-33.py
```

Follow the prompts to choose your password style, length, and optional pattern/scope.

## Requirements

- Python 3.6 or higher
- No external dependencies (standard library only)

## Roadmap

- [ ] Add CLI flag support
- [ ] Implement clipboard copy with secure timeout
- [ ] Expand input validation using `try` blocks
- [ ] Optional TUI mode
- [ ] Export as pip-installable package

## Author

Juan J. Garcia ([@0xjuang](https://github.com/0xjuang))  

## License

This project is licensed under the MIT License.
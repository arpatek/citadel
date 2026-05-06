# citadel

```
┌──────────────────────────────────────────────────────────────┐
│                          Citadel                             │
│             Pattern-Based Password Generator                 │
│                                                              │
│      Author: Juan Garcia (arpatek)                           │
│      Description: Generates secure passwords using           │
│                   patterns, scopes, and randomized entropy.  │
└──────────────────────────────────────────────────────────────┘
```

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)]()

**citadel** is a pattern-based password generator written in Python. It generates
structured, human-readable passwords with optional scope tagging and cryptographically
secure entropy — built for terminal-native workflows.

---

### Features

`[Cryptographically Secure]` Uses Python's `secrets` module — not `random` — for strong entropy.  
`[Pattern Support]` Three generation styles: fully random, pattern + random, pattern + scope + random.  
`[No Dependencies]` Standard library only — nothing to install.  
`[Input Validation]` Validates all prompts with retry loops.  

---

### Example Styles

```
[1] Random
    ➤ Example: w3#9Tf8z@L

[2] Pattern + Random
    ➤ Example: myPattern.-r@nd0m!

[3] Pattern + Scope + Random
    ➤ Example: myPattern.-github.r@nd0m!
```

---

### Usage

```bash
./citadel.py
```

Follow the prompts to choose a password style, length, and optional pattern/scope.

---

### Requirements

- Python 3.6+
- No external dependencies

---

### Roadmap

- [ ] Add CLI flag support via argparse
- [ ] Clipboard copy with secure timeout
- [ ] Optional TUI mode via Textual
- [ ] Export as pip-installable CLI package

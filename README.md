# MASA Cipher Mind

A tactical numeric decryption game challenging users to deduce pseudo-random target ciphers using real-time proximity heuristics.

## Technical Architecture

The codebase follows modular software engineering patterns and OOP structure, designed for reliability, high maintainability, and clean separation of concerns:

- **Component Layering**: User interface and computational state are decoupled into specialized controllers and event loops.
- **Defensive Engineering**: Comprehensive validation guards protect against malformed inputs and runtime exceptions.
- **Modern Design Tokens**: Designed with a high-contrast dark aesthetic adhering to modern developer tooling visual standards.

## Features

- Multi-tiered operational difficulty levels (Novice, Operative, CyberMaster).
- Dynamic proximity progress bar computing real-time mathematical distance.
- Attempt limitation system with win streak persistence across rounds.
- Custom keyboard shortcuts enabling rapid gameplay via Return key.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter
```

## Execution

Initialize and run the module via the command line:

```bash
python "Guess the Number Game Using Tkinter in Python/main.py"
```

## Project Structure

```
.
├── Guess the Number Game Using Tkinter in Python
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.

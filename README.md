# Python Terminal Game

A Pacman-like game written in Python using the Curses library for the terminal environment.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Contributing](#contributing)
- [License](#license)

## Description

This is a simple terminal-based game inspired by Pacman. The player navigates through a grid, collecting food and avoiding enemies. The game is implemented using the Curses library, which provides a way to create text-based user interfaces.

## Features

- Randomly generated game world with obstacles, food, and enemies
- Player movement and collision detection
- Score tracking
- Game over screen

## Installation

To run this game, you need to have Python installed on your system. Additionally, the Curses library is required.

> [!NOTE]
> Curses library is not available on Windows by default. You can use a Unix-based system or WSL to run the game on Windows.

Clone the repository:

```sh
git clone https://github.com/shayandelbari/python-terminal-game.git
cd python_terminal_game
```

## Usage

To start the game, run the following command:

```sh
python main.py
```

## Controls

- `W` - Move up
- `A` - Move left
- `S` - Move down
- `D` - Move right
- `Q` - Quit the game

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

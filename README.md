# Snake Game

A classic Snake game implementation using Python and Pygame.

## Features

- Classic snake gameplay with arrow key or WASD controls
- Score tracking
- Collision detection with walls and self
- Pause functionality (Space bar)
- Game over screen with restart option
- Clean, modular code structure

## Installation

1. Make sure you have Python 3.7 or higher installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the game with:
```bash
python main.py
```

## Controls

- **Arrow Keys** or **WASD**: Move the snake
- **Space**: Pause/Resume game
- **R**: Restart game (on game over screen)
- **ESC**: Quit game (on game over screen)

## Game Rules

- Control the snake to eat red food pellets
- Each food pellet increases your score by 10 points
- The snake grows longer each time it eats food
- Avoid hitting the walls or the snake's own body
- The game ends when the snake collides with a wall or itself

## Project Structure

```
snake-game/
├── main.py          # Main entry point and game loop
├── game.py          # Game class with game logic and state management
├── snake.py         # Snake class for player object
├── food.py          # Food class for collectible items
├── config.py        # Configuration constants and settings
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Customization

You can customize the game by modifying the constants in `config.py`:

- Window size and grid dimensions
- Colors
- Frame rate (game speed)
- Initial snake length
- And more!

## Development

The code is organized into separate modules for easy maintenance and extension:

- **main.py**: Contains the main game loop and Pygame initialization
- **game.py**: Handles game state, input processing, and rendering coordination
- **snake.py**: Manages snake movement, growth, and collision detection
- **food.py**: Handles food generation and rendering
- **config.py**: Centralizes all game configuration constants

Feel free to modify and extend the code to add new features!

## Future Enhancements

Some ideas for extending the game:
- High score system with persistent storage
- Different difficulty levels
- Sound effects and music
- Multiple food types with different point values
- Power-ups and special abilities
- Menu system
- Better graphics and animations
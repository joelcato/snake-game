"""
Configuration settings for the Snake game
"""

class Config:
    """Game configuration constants"""
    
    # Window dimensions
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    
    # Game grid settings
    GRID_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
    GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
    
    # Frame rate
    FPS = 10
    
    # Colors (RGB values)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 155, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)
    
    # Snake settings
    INITIAL_SNAKE_LENGTH = 3
    SNAKE_SPEED = 1  # Grid cells per frame
    
    # Game states
    GAME_PLAYING = "playing"
    GAME_OVER = "game_over"
    GAME_PAUSED = "paused"
    MENU = "menu"
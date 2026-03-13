"""
Snake class for the Snake game
Handles snake movement, growth, and collision detection
"""

import pygame
from config import Config

class Snake:
    """Snake player object"""
    
    def __init__(self):
        """Initialize the snake"""
        self.reset()
    
    def reset(self):
        """Reset snake to initial state"""
        # Starting position (center of screen)
        start_x = Config.GRID_WIDTH // 2
        start_y = Config.GRID_HEIGHT // 2
        
        # Snake body as list of (x, y) coordinates
        self.body = []
        for i in range(Config.INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))
        
        # Initial direction (moving right)
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        
        # Growth flag
        self.grow = False
    
    def update(self):
        """Update snake position"""
        # Update direction
        self.direction = self.next_direction
        
        # Get head position
        head_x, head_y = self.body[0]
        
        # Calculate new head position
        new_head = (
            head_x + self.direction[0],
            head_y + self.direction[1]
        )
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, direction):
        """Change snake direction (if valid)"""
        # Prevent reversing into itself
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.next_direction = direction
    
    def grow_snake(self):
        """Mark snake for growth on next update"""
        self.grow = True
    
    def check_collision(self):
        """Check for collisions with walls or self"""
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if (head_x < 0 or head_x >= Config.GRID_WIDTH or
            head_y < 0 or head_y >= Config.GRID_HEIGHT):
            return True
        
        # Check self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False
    
    def get_head_position(self):
        """Get the head position of the snake"""
        return self.body[0]
    
    def draw(self, screen):
        """Draw the snake on the screen"""
        for i, (x, y) in enumerate(self.body):
            # Calculate pixel position
            pixel_x = x * Config.GRID_SIZE
            pixel_y = y * Config.GRID_SIZE
            
            # Draw head slightly different than body
            if i == 0:  # Head
                pygame.draw.rect(screen, Config.DARK_GREEN,
                               (pixel_x, pixel_y, Config.GRID_SIZE, Config.GRID_SIZE))
            else:  # Body
                pygame.draw.rect(screen, Config.GREEN,
                               (pixel_x, pixel_y, Config.GRID_SIZE, Config.GRID_SIZE))
            
            # Draw border
            pygame.draw.rect(screen, Config.BLACK,
                           (pixel_x, pixel_y, Config.GRID_SIZE, Config.GRID_SIZE), 1)
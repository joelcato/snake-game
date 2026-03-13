"""
Food class for the Snake game
Handles food generation and rendering
"""

import pygame
import random
from config import Config

class Food:
    """Food object for the snake to eat"""
    
    def __init__(self):
        """Initialize food"""
        self.position = self.generate_position()
    
    def generate_position(self, snake_body=None):
        """Generate a new random position for food"""
        while True:
            x = random.randint(0, Config.GRID_WIDTH - 1)
            y = random.randint(0, Config.GRID_HEIGHT - 1)
            position = (x, y)
            
            # Make sure food doesn't spawn on snake
            if snake_body is None or position not in snake_body:
                self.position = position
                return position
    
    def draw(self, screen):
        """Draw the food on the screen"""
        x, y = self.position
        pixel_x = x * Config.GRID_SIZE
        pixel_y = y * Config.GRID_SIZE
        
        # Draw food as red circle
        center = (pixel_x + Config.GRID_SIZE // 2, pixel_y + Config.GRID_SIZE // 2)
        radius = Config.GRID_SIZE // 2 - 1
        pygame.draw.circle(screen, Config.RED, center, radius)
    
    def get_position(self):
        """Get current food position"""
        return self.position
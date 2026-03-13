#!/usr/bin/env python3
"""
Snake Game - Main Entry Point
A classic Snake game implementation using Pygame
"""

import pygame
import sys
from game import Game
from config import Config

def main():
    """Main function to run the Snake game"""
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    
    # Create clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Create game instance
    game = Game(screen)
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game.handle_input(event.key)
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw()
        
        # Control frame rate
        clock.tick(Config.FPS)
    
    # Quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
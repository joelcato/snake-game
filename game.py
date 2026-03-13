"""
Main Game class for the Snake game
Handles game logic, state management, and rendering
"""

import pygame
from snake import Snake
from food import Food
from config import Config

class Game:
    """Main game controller"""
    
    def __init__(self, screen):
        """Initialize the game"""
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset_game()
    
    def reset_game(self):
        """Reset game to initial state"""
        self.snake = Snake()
        self.food = Food()
        self.food.generate_position(self.snake.body)
        self.score = 0
        self.game_state = Config.GAME_PLAYING
    
    def handle_input(self, key):
        """Handle keyboard input"""
        if self.game_state == Config.GAME_PLAYING:
            # Movement controls
            if key == pygame.K_UP or key == pygame.K_w:
                self.snake.change_direction((0, -1))
            elif key == pygame.K_DOWN or key == pygame.K_s:
                self.snake.change_direction((0, 1))
            elif key == pygame.K_LEFT or key == pygame.K_a:
                self.snake.change_direction((-1, 0))
            elif key == pygame.K_RIGHT or key == pygame.K_d:
                self.snake.change_direction((1, 0))
            elif key == pygame.K_SPACE:
                self.game_state = Config.GAME_PAUSED
        
        elif self.game_state == Config.GAME_PAUSED:
            if key == pygame.K_SPACE:
                self.game_state = Config.GAME_PLAYING
        
        elif self.game_state == Config.GAME_OVER:
            if key == pygame.K_r:
                self.reset_game()
            elif key == pygame.K_ESCAPE:
                return False  # Quit game
        
        return True
    
    def update(self):
        """Update game state"""
        if self.game_state != Config.GAME_PLAYING:
            return
        
        # Update snake
        self.snake.update()
        
        # Check for collision with food
        if self.snake.get_head_position() == self.food.get_position():
            self.snake.grow_snake()
            self.score += 10
            self.food.generate_position(self.snake.body)
        
        # Check for collisions
        if self.snake.check_collision():
            self.game_state = Config.GAME_OVER
    
    def draw(self):
        """Draw everything on screen"""
        # Clear screen
        self.screen.fill(Config.BLACK)
        
        if self.game_state == Config.GAME_PLAYING or self.game_state == Config.GAME_PAUSED:
            # Draw game objects
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            
            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, Config.WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Draw pause message if paused
            if self.game_state == Config.GAME_PAUSED:
                pause_text = self.font.render("PAUSED - Press SPACE to continue", True, Config.WHITE)
                text_rect = pause_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2))
                self.screen.blit(pause_text, text_rect)
        
        elif self.game_state == Config.GAME_OVER:
            self.draw_game_over()
        
        # Update display
        pygame.display.flip()
    
    def draw_game_over(self):
        """Draw game over screen"""
        # Game over text
        game_over_text = self.font.render("GAME OVER", True, Config.RED)
        game_over_rect = game_over_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2 - 60))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font.render(f"Final Score: {self.score}", True, Config.WHITE)
        score_rect = score_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2 - 20))
        self.screen.blit(score_text, score_rect)
        
        # Instructions
        restart_text = self.small_font.render("Press R to restart or ESC to quit", True, Config.WHITE)
        restart_rect = restart_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2 + 20))
        self.screen.blit(restart_text, restart_rect)
    
    def get_score(self):
        """Get current score"""
        return self.score
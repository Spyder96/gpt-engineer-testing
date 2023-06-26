import pygame

class GameView:
    def __init__(self, width: int, height: int):
        """Initializes the game window"""
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")

    def draw_snake(self, snake: Snake):
        """Draws the snake on the screen"""
        for segment in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0]*10, segment[1]*10, 10, 10))

    def draw_food(self, food: Food):
        """Draws the food on the screen"""
        pygame.draw.rect(self.screen, (255, 0, 0), (food.position[0]*10, food.position[1]*10, 10, 10))

    def draw_game_over(self):
        """Draws the game over screen"""
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

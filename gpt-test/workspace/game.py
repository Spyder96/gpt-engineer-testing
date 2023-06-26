from snake import Snake
import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.score = 0
        self.game_over = False

    def update(self):
        self.snake.move()
        if self.snake.is_colliding_with_wall(self.width, self.height) or self.snake.is_colliding_with_self():
            self.game_over = True
        elif self.snake.is_colliding_with_food():
            self.snake.grow()
            self.score += 1
            self.snake.generate_food(self.width, self.height)

    def get_score(self):
        return self.score

    def is_game_over(self):
        return self.game_over

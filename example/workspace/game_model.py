from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Snake:
    body: List[Tuple[int, int]]
    direction: Tuple[int, int]

    def move(self):
        """Moves the snake in the current direction"""
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def check_collision(self, width: int, height: int) -> bool:
        """Checks if the snake has collided with the walls or itself"""
        head = self.body[0]
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            return True
        if head in self.body[1:]:
            return True
        return False

@dataclass
class Food:
    position: Tuple[int, int]

    def generate_position(self, width: int, height: int):
        """Generates a new random position for the food"""
        self.position = (random.randint(0, width-1), random.randint(0, height-1))

    def check_collision(self, snake: Snake) -> bool:
        """Checks if the food has collided with the snake"""
        return self.position == snake.body[0]

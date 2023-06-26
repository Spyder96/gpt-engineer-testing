import pygame

class View:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = 10
        self.screen = pygame.display.set_mode((self.width * self.block_size, self.height * self.block_size))
        pygame.display.set_caption("Snake")

    def draw(self, snake, score):
        self.screen.fill((0, 0, 0))
        for block in snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), (block[0] * self.block_size, block[1] * self.block_size, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (snake.food[0] * self.block_size, snake.food[1] * self.block_size, self.block_size, self.block_size))
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        pygame.display.update()

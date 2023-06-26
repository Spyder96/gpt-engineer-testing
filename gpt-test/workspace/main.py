import pygame
from game import Game
from view import View

def main():
    pygame.init()
    width = 40
    height = 30
    game = Game(width, height)
    view = View(width, height)
    clock = pygame.time.Clock()

    while not game.is_game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction != "down":
                    game.snake.direction = "up"
                elif event.key == pygame.K_DOWN and game.snake.direction != "up":
                    game.snake.direction = "down"
                elif event.key == pygame.K_LEFT and game.snake.direction != "right":
                    game.snake.direction = "left"
                elif event.key == pygame.K_RIGHT and game.snake.direction != "left":
                    game.snake.direction = "right"

        game.update()
        view.draw(game.snake, game.get_score())
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()

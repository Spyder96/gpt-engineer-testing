import pygame

class GameController:
    def __init__(self, snake: Snake, food: Food):
        """Initializes the game controller"""
        self.snake = snake
        self.food = food

    def handle_input(self):
        """Handles user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)

    def update(self):
        """Updates the game state"""
        self.snake.move()
        if self.food.check_collision(self.snake):
            self.snake.body.append(self.food.position)
            self.food.generate_position(self.width, self.height)
        if self.snake.check_collision(self.width, self.height):
            self.game_over = True

    def run(self, width: int, height: int):
        """Runs the game loop"""
        pygame.init()
        self.width = width
        self.height = height
        self.game_over = False
        clock = pygame.time.Clock()
        self.food.generate_position(width, height)
        while not self.game_over:
            clock.tick(10)
            self.handle_input()
            self.update()
            self.screen.fill((0, 0, 0))
            self.view.draw_snake(self.snake)
            self.view.draw_food(self.food)
            pygame.display.update()
        self.view.draw_game_over()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

from game_model import Snake, Food
from game_view import GameView
from game_controller import GameController

def main():
    snake = Snake([(5, 5), (4, 5), (3, 5)], (1, 0))
    food = Food((0, 0))
    view = GameView(500, 500)
    controller = GameController(snake, food, view)
    controller.run(50, 50)

if __name__ == "__main__":
    main()

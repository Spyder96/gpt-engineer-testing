import random

class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = "right"
        self.food = self.generate_food()

    def move(self):
        head = self.body[-1]
        if self.direction == "right":
            new_head = (head[0] + 1, head[1])
        elif self.direction == "left":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "up":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "down":
            new_head = (head[0], head[1] + 1)
        self.body.append(new_head)
        if new_head != self.food:
            self.body.pop(0)
        else:
            self.generate_food()

    def generate_food(self, width, height):
        while True:
            food = (random.randint(0, width - 1), random.randint(0, height - 1))
            if food not in self.body:
                self.food = food
                break

    def grow(self):
        self.body.append(self.body[-1])

    def is_colliding_with_wall(self, width, height):
        head = self.body[-1]
        return head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height

    def is_colliding_with_self(self):
        head = self.body[-1]
        return head in self.body[:-1]

    def is_colliding_with_food(self):
        head = self.body[-1]
        return head == self.food

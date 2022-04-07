import collections
class SnakeGame:
    def __init__(self, width, height, food):
        self.cols = width
        self.rows = height
        self.food = collections.deque(food) # pop left if eat the food
        self.snake = collections.deque((0, 0)) # appendleft the food as the new head
        self.directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)} 
    
    def move(self, direction):
        r, c = self.directions[direction]
        # head is always left-most of the deque
        new_head = [self.snake[0][0] + r, self.snake[0][1] + c]

        # game is over
        # either new head out of boundary or new head hit its body (notice hit tail is allowed)
        if (new_head[0] < 0 or new_head[0] >= self.rows) or (new_head[1] < 0 or new_head[1] >= self.cols) or ((new_head in self.snake) and (new_head != self.snake[-1])):
            return -1

        # if there is food, eat the food and make the food be part of the snake body
        if self.food and (new_head == self.food[0]):
            self.snake.appendleft(new_head)
            self.food.popleft()
        # if there is no food, move ahead as new head added and old tail removed to keep the snake length
        else:
            self.snake.appendleft(new_head)
            self.snake.pop()

        # final score should be deducted by the initial snake length
        return len(self.snake) - 1


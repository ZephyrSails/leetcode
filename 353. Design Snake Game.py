class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = list(reversed(food))
        self.dirMap = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.length = 1
        self.snake = collections.deque([[0, 0]])
        self.snakeSet = set([(0, 0)])


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if self.length == -1: return -1
        oldHead = self.snake[-1]
        head = [oldHead[0] + self.dirMap[direction][0], oldHead[1] + self.dirMap[direction][1]]
        # print self.head
        if head[0] < 0 or head[0] >= self.height or head[1] < 0 or head[1] >= self.width:
            self.length = -1
            return -1

        if tuple(head) in self.snakeSet:
            if head == self.snake[0]:
                self.snake.append(self.snake.popleft())
                return self.length - 1
            else:
                self.length = -1
                return -1

        if self.food and head == self.food[-1]:
            self.food.pop()
            self.snake.append(head)
            self.snakeSet.add(tuple(head))
            self.length += 1
        else:
            self.snakeSet.remove(tuple(self.snake.popleft()))
            self.snake.append(head)
            self.snakeSet.add(tuple(head))

        return self.length - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

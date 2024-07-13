from random import randint
import turtle

class Maze:
    def __init__(self, dim):
        self.dim = dim
        self.listt = [-1] * (dim * dim)
        self.d = turtle.Turtle()

    def find(self, x):
        while self.listt[x] > 0:
            x = self.listt[x]
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.listt[root_a] <= self.listt[root_b]:
                self.listt[root_a] += self.listt[root_b]
                self.listt[root_b] = root_a
            else:
                self.listt[root_b] += self.listt[root_a]
                self.listt[root_a] = root_b

    def draw(self, x, y, x1, y1):
        self.d.penup()
        self.d.goto(x, y)
        self.d.pendown()
        self.d.goto(x1, y1)

    def draw_maze(self, walls):

        for i in walls:
            if i[1] == i[0] + 1:  # right wall
                x = (i[0] % self.dim) * 20
                y = (self.dim - (i[0] // self.dim)) * 20
                self.draw(x + 20, y, x + 20, y - 20)
            else:  # bottom wall
                x = (i[0] % self.dim) * 20
                y = (self.dim - (i[0] // self.dim)) * 20
                self.draw(x, y - 20, x + 20, y - 20)
        self.draw(0, 0, self.dim * 20, 0)
        self.draw(self.dim * 20, 0, self.dim * 20, self.dim * 20)
        self.draw(self.dim * 20, self.dim * 20, 0, self.dim * 20)
        self.draw(0, self.dim * 20, 0, 0)
        s = self.d.getscreen()
        s.mainloop()


def adjacent_list(dim):
    arr = []
    for i in range(dim * dim):
        if (i + 1) % dim != 0:  # right neighbor
            arr.append([i, i + 1])
        if i + dim < dim * dim:  # bottom neighbor
            arr.append([i, i + dim])
    return arr

k= 12
m = Maze(k)

values = adjacent_list(k)
while m.find(0) != m.find(k * k - 1):
    if len(values) == 0:
        break
    random = randint(0, len(values) - 1)
    m.union(values[random][0], values[random][1])
    values.pop(random)

m.draw_maze(values)

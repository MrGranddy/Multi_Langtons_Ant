import pygame
import numpy as np
from numpy.random import rand
from random import randrange


background_color = (240, 240, 240)
(width, height) = (1000, 1000)
DARK_WHITE = (150, 150, 150)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Langton's Ant")
screen.fill(background_color)

print('Please enter the number of colors: ')
number_of_colors = int(input())
print('Please enter the number of ants: ')
number_of_ants = int(input())

color_rotations = []
colors = []

for i in range(number_of_colors):
    prob = rand()
    if prob < 0.5:
        color_rotations += [1]
    else:
        color_rotations += [-1]
    colors += [(randrange(0, 256), randrange(0, 256), randrange(0, 256))]

mapped_colors = []

for i in range(500):
    row = []
    for j in range(500):
        row += [1]
    mapped_colors += [row]

#       0
#       |
#       |
# 3 --- * --- 1
#       |
#       |
#       2


class Ant:

    def __init__(self, starting_point):
        self.x = starting_point[0]
        self.y = starting_point[1]
        self.direction = 0

    def redirect(self):
        print(self.x, self.y)
        curr_color = mapped_colors[self.x][self.y]
        rotation = color_rotations[curr_color]
        if rotation == -1:
            if self.direction == 0:
                self.direction = 3
            else:
                self.direction -= 1
        elif rotation == 1:
            if self.direction == 3:
                self.direction = 0
            else:
                self.direction += 1

    def colorize(self):
        if mapped_colors[self.x][self.y] == number_of_colors - 1:
            mapped_colors[self.x][self.y] = 0
        else:
            mapped_colors[self.x][self.y] += 1
        color = mapped_colors[self.x][self.y]
        rect = pygame.Rect((self.x * 2 + 1, self.y * 2 + 1), (2, 2))
        pygame.draw.rect(screen, colors[color], rect)
        return rect

    def move(self):
        if self.direction == 0:
            if self.y == 499:
                self.y = -1
            self.y += 1
        elif self.direction == 1:
            if self.x == 499:
                self.x = -1
            self.x += 1
        elif self.direction == 2:
            if self.y == 0:
                self.y = 500
            self.y -= 1
        else:
            if self.x == 0:
                self.x = 500
            self.x -= 1

    def step(self):
        self.redirect()
        rect = self.colorize()
        self.move()
        return rect

# for i in range(500):
    #pygame.draw.line(screen, DARK_WHITE, (i * 2, 0), (i * 2, 1000), 1)
    #pygame.draw.line(screen, DARK_WHITE, (0, i * 2), (1000, i * 2), 1)

ants = []
for i in range(number_of_ants):
    ants += [Ant((randrange(10, 490), randrange(10, 490)))]

running = True
cycle = 0
while running:
    print('Cycle', cycle)
    cycle += 1
    rect = []
    for ant in ants:
        rect += [ant.step()]
    pygame.display.update(rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

import pygame
import sys
#from pygame import mixer
#import time
import pandas
#import math
import random

#using a really bad youtube tutorial

# implementing each of the squares in the NxM maze
class Node: #the square in the maze (pixles x pixles)
    def __init__(self, row, col, size):
        self.m_row = row
        self.m_col = col
        self.m_size = size
        self.m_walls = {} #key is north, south, west, east and value is adjacent Node

    def connections(self):
        m_list = []
        for key,val in self.m_valls.items():
            if val != None:
                m_list.append(key)
        return m_list

    def draw(self, screen):
        pass

class Maze:
    def __init__(self, num_rows, num_cols, node_size):
        self.m_num_rows = num_rows
        self.m_num_cols = num_cols
        self.m_node_size = node_size
        self.m_nodes = [ [Node(i, j, self.m_node_size)
                          for j in range(self.m_num_cols)] \
                         for i in range(self.m_num_rows)]  # 2 dimensional array of nodes


    def connect_nodes_default(self):
        for node in self.iter_node(): #generator
            node.m_walls['north'] = self.get_node(node.m_row -1, node.my_col)
            node.m_walls['south'] = self.get_node(node.m_row + 1, node.my_col)
            node.m_walls['west'] = self.get_node(node.m_row, node.my_col -1)
            node.m_walls['east'] = self.get_node(node.m_row, node.my_col +1)


    def get_node(self, row, col):
        if row >= 0 and row < self.m_num_rows \
            and col >= 0 and col < self.m_num_cols:
            return self.m_nodes[row][col]
        else:
            return None

    def draw(self, screen):
        self.draw_outer_boundary(screen)
        for node in self.iter_node():
            node.draw(screen)

    def draw_outer_boundary(self, screen):
        topleft = (self.m_node_size, self.m_node_size)
        topright = (self.m_node_size + self.m_node_size*self.m_num_cols, self.m_node_size)
        bottomleft = (self.m_node_size, self.m_node_size + self.m_node_size * self.m_num_rows)
        bottomright = (self.m_node_size + self.m_node_size*self.m_num_cols, \
                       self.m_node_size + self.m_node_size * self.m_num_rows)

    pygame.draw.line(screen, (0,0,0), topleft, topright, 5)
    pygame.draw.line(screen, (0,0,0), topleft, bottomleft, 5)
    pygame.draw.line(screen, (0,0,0), topright, bottomright, 5)
    pygame.draw.line(screen, (0,0,0), bottomleft, bottomright, 5)

    def iter_node(self):
        for i in range(self.m_num_rows):
            for j in range(self.m_num_cols):
                yield self.m_nodes[i][j]

    def printme(self):
        for node in self.iter_node():
            print(node.m_row, node.m_col, node.connections())

# Intitializing game
def main():
    pygame.init()
    screen = pygame.display.set_mode((900,900), 0, 32)
    screen.fill((255,255,255)) #white screen

    num_rows = 6
    num_cols = 6
    node_size = 30
    maze = Maze(num_rows, num_cols, node_size)
    maze.connect_nodes_default() #creating walls in each node (dict)
    maze.draw(screen)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
    sys.exit()







# Making food
#food_img = pygame.image.load("pizza48.png")
#food_x = random.randint(10, 944)
#food_y = random.randint(10, 584)

#def food(x, y):
 #   screen.blit(food_img, (x, y))

#def isCollision_food(cursor_pos, foodX, foodY):
 #   distance = math.sqrt((math.pow(cursor_pos[x] - foodX, 2)) + (math.pow(cursor_pos[y] - foodY, 2)))
  #  if distance < 27:
   #     return True
   # else:
    #    return False



#icon_rect = icon.get_rect()
#icon_rect.center = pygame.mouse.get_pos()
#screen.blit(cursor, cursor_rect)

#log = pandas.DataFrame(columns=["Count", "Snake_x", "Snake_y", "Snake_angle"])

#size = (24,24)
#pygame.mouse.set_cursor(size, icon)
#pygame.display.set_icon(icon)

#pygame.mouse.set_cursor(icon)
# Loosing image:
#losingIMG = pygame.image.load("game-over.png")

# Making a mouse - the cursor
#mouse_img = pygame.image.load("mouse.png")
#mouse_pos = pygame.mouse.get_pos()
#mouseX = 480
#mouseY = 300
#mouseX_change = 0
#mouseY_change = 0

# Defining functions
#def mouse(x, y):
 #   position = pygame.mouse.set_pos(0,0)
  #  screen.blit(position, (x, y))


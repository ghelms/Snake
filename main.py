import pygame
import time

# Intitialize game
pygame.init()

# Create the screen
screen_x = 960
screen_y=640
screen = pygame.display.set_mode((screen_x, screen_y))

# Background
background = pygame.image.load("grass.jpg")

# Title and icon
pygame.display.set_caption("Snake invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Loosing image:
losingIMG = pygame.image.load("game-over.png")

# Making a snake
snake_img = pygame.image.load("brain.png")
snake_angle = 0
snakeX = 480
snakeY = 320
snakeX_change = 0
snakeY_change = 0

#making a tail
tail_img = pygame.image.load("neuron.png")
tail_img = pygame.transform.rotate(tail_img, 315)
tail_x_change = 0
tail_y_change = 22


def snake(x, y, angle):
    surf = pygame.transform.rotate(snake_img,angle)
    screen.blit(surf, (x,y))

def tail(x,y,angle,x_change,y_change):
    surf_tail = pygame.transform.rotate(tail_img, angle)
    screen.blit(surf_tail, (x+x_change,y+y_change))

count = 1
# Game loop
running = True
lose = False
win = False
while running:

    # RGB - (MAKING IT BLACK)
    screen.fill((255, 255, 255))

    # Adding background
    #screen.blit(background, (0, 0))

    # Looping through events
    for event in pygame.event.get():

        # Making sure we can quit the game
        if event.type == pygame.QUIT:
            running = False

        # Making the snake move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeX_change = -0.2
                snakeY_change = 0
                snake_angle = 90
                tail_x_change = 22
                tail_y_change = -4
            if event.key == pygame.K_RIGHT:
                snakeX_change = 0.2
                snakeY_change = 0
                snake_angle = 270
                tail_x_change = -30
                tail_y_change = -4
            if event.key == pygame.K_UP:
                snakeY_change = -0.2
                snakeX_change = 0
                snake_angle = 0
                tail_x_change = -4
                tail_y_change = 22
            if event.key == pygame.K_DOWN:
                snakeY_change = 0.2
                snakeX_change = 0
                snake_angle = 180
                tail_x_change = -4
                tail_y_change = -30
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

    # Adding new coordinates to snakes position
    snakeX += snakeX_change
    snakeY += snakeY_change

    # Making a border:
    if snakeX <= 0:
        snakeX = 0
        lose = True
    elif snakeX >= 936:
        snakeX = 936
        lose = True

    if snakeY <= 0:
        snakeY = 0
        lose = True
    elif snakeY >= 616:
        snakeY = 616
        lose = True

    # Updating snake position
    snake(snakeX, snakeY, snake_angle)

    #updating tail position
    tail(snakeX, snakeY, snake_angle, tail_x_change, tail_y_change)

    #IF LOST TEXT
    if lose == True:
        screen.blit(losingIMG, (224, 64))
        pygame.display.update()
        time.sleep(2)
        running = False
    count += 0.001
    screen = pygame.display.set_mode((screen_x-count,screen_y-count))
    screen.blit
    if screen_y <= 0:
        running = False

    # Update the screen
    pygame.display.update()

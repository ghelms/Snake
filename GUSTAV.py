import pygame
import time
import pandas

# Intitializing game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((960, 640))

# Background
background = pygame.image.load("grass.jpg")

# Title and icon
pygame.display.set_caption("Snake invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Loosing image:
losingIMG = pygame.image.load("game-over.png")

# Making a snake
snake_img = pygame.image.load("brain.png")
snake_angle = 0
snakeX = 480
snakeY = 320
snakeX_change = 0
snakeY_change = 0

# making a tail
tail_img = pygame.image.load("neuron.png")
tail_x = 0
tail_y = 0
tail_angle = 0

# Making an empty dataframe for logging the coordinates with 18 rows of the start position
log = pandas.DataFrame(columns=["Count", "Snake_x", "Snake_y", "Snake_angle"])
for i in range(1, 18):
    log = log.append({
        "Count": i,
        "Snake_x": 480,
        "Snake_y": 320,
        "Snake_angle": 0
    }, ignore_index=True)

# Making a counter
counter = 18


# Defining functions
def snake(x, y, angle):
    surf = pygame.transform.rotate(snake_img, angle)
    screen.blit(surf, (x, y))


def tail(x, y, angle):
    surf_tail = pygame.transform.rotate(tail_img, angle)
    screen.blit(surf_tail, (x, y))


# Game loop
running = True
lose = False
win = False

while running:

    # RGB - (MAKING IT WHITE)
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
                snakeX_change = -2
                snakeY_change = 0
                snake_angle = 90
            if event.key == pygame.K_RIGHT:
                snakeX_change = 2
                snakeY_change = 0
                snake_angle = 270
            if event.key == pygame.K_UP:
                snakeY_change = -2
                snakeX_change = 0
                snake_angle = 0
            if event.key == pygame.K_DOWN:
                snakeY_change = 2
                snakeX_change = 0
                snake_angle = 180
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

    # Adding new coordinates to snakes position and counter
    snakeX += snakeX_change
    snakeY += snakeY_change
    counter += 1

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

    # Adding all the snake data to the logfile
    log = log.append({
        "Count": counter,
        "Snake_x": snakeX,
        "Snake_y": snakeY,
        "Snake_angle": snake_angle
    }, ignore_index=True)

    #The coordinates for the tail are the same as the ones for the snake 18 loops ago. This is done by indexing.
    tail_x = log["Snake_x"][log["Count"][counter - 18]]
    tail_y = log["Snake_y"][log["Count"][counter - 18]]
    tail_angle = log["Snake_angle"][log["Count"][counter - 18]]

    # updating tail position
    tail(tail_x, tail_y, tail_angle)

    # Removing redundant lines in the logfile
    #length_log = len(log["Count"])
    #print(length_log)
    #if length_log >= 30:
    #    log = log.drop(0)

    # IF LOST - TEXT
    if lose:
        screen.blit(losingIMG, (224, 64))
        pygame.display.update()
        time.sleep(2)
        running = False

    # Update the screen
    pygame.display.update()

print(log)


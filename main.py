import pygame

# Intitialize game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((960, 640))

# Background
background = pygame.image.load("grass.jpg")

# Title and icon
pygame.display.set_caption("Snake invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Loosing image:
losingIMG = pygame.image.load()

# Making a snake
snakeIMG = pygame.image.load("brain.png")
snakeX = 480
snakeY = 320
snakeX_change = 0
snakeY_change = 0


def snake(x, y):
    screen.blit(snakeIMG, (x, y))

def YOU_LOSE():
    screen.blit(losingIMG, (50,50))
    running = False

# Game loop
running = True
while running:

    # RGB - (MAKING IT BLACK)
    screen.fill((0, 0, 0))

    # Adding background
    screen.blit(background, (0, 0))

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
            if event.key == pygame.K_RIGHT:
                snakeX_change = 2
                snakeY_change = 0
            if event.key == pygame.K_UP:
                snakeY_change = -2
                snakeX_change = 0
            if event.key == pygame.K_DOWN:
                snakeY_change = 2
                snakeX_change = 0
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
    snake(snakeX, snakeY)

    #IF LOST TEXT
    if lose == True:
        YOU_LOSE()

    # Update the screen
    pygame.display.update()

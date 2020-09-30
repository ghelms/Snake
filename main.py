import pygame

# Intitialize game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((450, 450))

# Background
background = pygame.image.load("grass.jpg")

# Title and icon
pygame.display.set_caption("Snake invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

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

    # Update the screen
    pygame.display.update()

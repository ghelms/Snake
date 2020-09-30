import pygame


#Initialize game
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Create a background
Background = pygame.image.load("background.png")

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("32.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("64.png")
playerX = 380
playerY = 480
playerX_change = 0

# Enemy

#bullet


#Making functions for the game:
def player(x,y):
    screen.blit(playerImg, (x, y))


#Game loop
running = True
while running:

    #Screen fill RGB - Red, Green, Blue
    screen.fill((0,0,0))

    #Adding background
    screen.blit(Background, (0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
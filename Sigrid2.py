import pygame, random, math

# initializing game

pygame.init()

# Create the screen
screen = pygame.display.set_mode((960, 600))

# Clock
clock = pygame.time.Clock()

# Background
#background = screen.fill((255, 255, 255)) #making it white
cheese_bg = pygame.image.load('cheese.jpg')

# Background sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Title and icon (cursos)
pygame.display.set_caption("Mouse maze")
icon = pygame.image.load("mouse48.png")
cursor_x = pygame.mouse.get_pos()[0] #get the position of the cursor
cursor_y = pygame.mouse.get_pos()[1]
pygame.mouse.set_visible(False) #makes mouse invisible

# make a square
color = (0, 0, 0)
square_x = random.randint(10, 944)
square_y = random.randint(10, 584)

# make surprise
pizza = pygame.image.load('pizza48.png')

def isCollision_square(cursor_x, cursor_y, square_X, square_Y):
    distance = math.sqrt((math.pow(cursor_x - square_X, 2)) + (math.pow(cursor_y - square_Y, 2)))
    if distance < 27:
        return True
    else:
        return False

# main loop
running = True

while running:
    pygame.time.delay(100)

#making sure we can quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 #making the background
    screen.blit(cheese_bg, (-20,0))

    #drawing icon
    screen.blit(icon, (pygame.mouse.get_pos()))

    #screen.blit(square, square_x, square_y)

    pygame.draw.rect(screen, color, pygame.Rect(square_x, square_y, 24, 24))

    # Collision
    collision_square = isCollision_square(cursor_x,cursor_y, square_x, square_y)
    if collision_square:
        screen.blit(pizza, (0,0))
        running = False

    #pygame.draw(screen)
    pygame.display.update() #update the screen with the content of the while loop

#limiting the framerate (not too fast)
    clock.tick(120) #120 = frames per second

pygame.quit()


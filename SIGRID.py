import pygame
#from pygame import mixer
#import time
import pandas
#import math
import random

# Intitializing game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((960, 600))

#clock
clock = pygame.time.Clock()

# Background
background = screen.fill((255, 255, 255))
cheese_bg = pygame.image.load('cheese.jpg')

# Background sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Title and icon (cursos)
pygame.display.set_caption("Mouse maze")
icon = pygame.image.load("mouse48.png")
cursor_pos = pygame.mouse.get_pos() #get the position of the cursor
pygame.mouse.set_visible(False) #makes mouse invisible

# Making food
food_img = pygame.image.load("pizza48.png")
food_x = random.randint(10, 944)
food_y = random.randint(10, 584)

def food(x, y):
    screen.blit(food_img, (x, y))

#def isCollision_food(cursor_pos, foodX, foodY):
 #   distance = math.sqrt((math.pow(cursor_pos[x] - foodX, 2)) + (math.pow(cursor_pos[y] - foodY, 2)))
  #  if distance < 27:
   #     return True
   # else:
    #    return False


# main loop
running = True

while running:
    pygame.time.delay(100)

#making sure we can quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# making the background white
    screen.fill((255, 255, 255))

    screen.blit(cheese_bg, (-20,0))

    #drawing icon
    screen.blit(icon, (pygame.mouse.get_pos()))

    # Adding the food
    food(food_x, food_y)

    # Collision
    #collision_food = isCollision_food(cursor_pos, food_x, food_y)
    #if collision_food:
        #eating_sound = mixer.Sound("explosion.wav")
        #eating_sound.play()
        #no_tails += 1
        #score_value += 1
        #food_x = random.randint(10, 944)
        #food_y = random.randint(10, 584)

    #pygame.draw(screen)
    pygame.display.update() #update the screen with the content of the while loop

#limiting the framerate (not too fast)
    clock.tick(120) #120 = frames per second

pygame.quit()



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



# Game loop
#running = True
#lose = False
#win = False

#while running:

    # RGB - (MAKING IT WHITE)
    #screen.fill((255, 255, 255))

    # Adding background
   # screen.blit(background, (0, 0))

    # Looping through events
    #for event in pygame.event.get():

        # Making sure we can quit the game
     #   if event.type == pygame.QUIT:
      #      running = False
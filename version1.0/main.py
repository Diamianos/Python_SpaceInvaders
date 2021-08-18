import pygame
import os.path
import random
import math

filepath = os.path.dirname(__file__) # Directory of the current working folder

# Intitalize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600)) 

# Background image
bg = pygame.image.load(os.path.join(filepath, "background.png"))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join(filepath, "ufo.png")) # Website for free png images ( for icons needs to be 32 x 32 pixels) https://www.flaticon.com/
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(os.path.join(filepath, "player.png"))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg_large = pygame.image.load(os.path.join(filepath, "enemy.png"))
enemyImg = pygame.transform.scale(enemyImg_large, (48, 48)) # modifying the size of the enemy image
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40

# Bullet

# Ready - you cant see the bullet on the screen
# Fire - the bullet is currently moving 
bulletImg = pygame.image.load(os.path.join(filepath, "bullet.png"))
bulletY = 480
bulletX = 0
bulletY_change = 10
bullet_state = "ready"
score = 0

# Function to draw the player ship
def player(x, y): # 2 variables to pass the x and y cordinate changes 
    screen.blit(playerImg, (x, y)) # Drawing the image on the screen. Takes 2 variables, the entitiy and its position


# Functon to draw the enemy
def enemy(x,y):
    screen.blit(enemyImg, (x, y))


# Bullet Function 
def fire_bullet(x, y):
    global bullet_state # Ability to use bullet in while loop
    bullet_state = "fire" # Changing bullet state to fire to shoot the bullet
    screen.blit(bulletImg, (x + 16,y + 10)) # Drawing the bullet on screen and adding values to x and y cordiante 

def isCollision (enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt ((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2))) # Forumula to calculate distance between two end points
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True # Condition to keep game running
while running: # Main while loop
    
    # Load background image
    
    screen.blit(bg, (0, 0))

    for event in pygame.event.get(): #for loop to check the events that are happening
        # Close game event
        if event.type == pygame.QUIT: # If closed button is pressed
            running = False # Change variable running to equal False to close out of program 
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5 # decreasing x position by 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 5 # increasing x position by 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # Checking when keystroke is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of space ship so it doesn't go out of bounds

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)


    player(playerX, playerY) # Calling the player function and giving the starter cordinates
    enemy(enemyX, enemyY)
    pygame.display.update() # Updating the game screen

    #End Time 1:44:00
    # https://www.youtube.com/watch?v=FfWpgLFMI7w&t=3769s
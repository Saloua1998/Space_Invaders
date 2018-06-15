# Add collision so the space shuttle can't leave the space image
# Add Bullets
    # You can fire one bullet at a time
    # You can shot multiple bullets
    # If the Bullet hits the window it should be deleted
# Add Monsters
    # Upload a monster image
    # The monster must move forward
    # The monsters must be spawn once per 2 seconds
    # When a bullet hits a monster the image must be deleted
    # When the monster hit the player it must explode (make 2 more images for explotion effect
# Add 3 Life points
    # If a monster hits you one life point is lost
    # When you lost 3 life points add in big letters LOST!
# Add score
    # Make a variable called Score
    # Every time the player kills a monster 1 point must be added to score
    # The score must be shown at the top left of the screen

# Add Highscore
# Add Levels
# Add a startscreen
# Add options on the top right
# Add Bosses
import pygame

# Initialize the game engine
pygame.init()

# Display
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("SPACE INVADERS")

# Images
Background = pygame.image.load("Space.jpg")
Background = pygame.transform.scale(Background, (1400, 600))

Space_Shuttle = pygame.image.load("Space_Shuttle.png")
Space_Shuttle = pygame.transform.scale(Space_Shuttle, (100, 130))

# Colors
black = 0, 0, 0
yellow = 238, 201, 0

# Variables
x_Space_Shuttle = 0
x_Space_Shuttle_Speed = 0
y_Space_Shuttle = 300
y_Space_Shuttle_Speed = 0

x_Shot = x_Space_Shuttle

Condition = False

while not Condition:

    x_Space_Shuttle += x_Space_Shuttle_Speed
    y_Space_Shuttle += y_Space_Shuttle_Speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Condition = True

    # Keys to move the space shuttle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            x_Space_Shuttle_Speed = 5
        if event.key == pygame.K_a:
            x_Space_Shuttle_Speed = -5
        if event.key == pygame.K_w:
            y_Space_Shuttle_Speed = -5
        if event.key == pygame.K_s:
            y_Space_Shuttle_Speed = 5
        if event.key == pygame.K_SPACE:
            None

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            x_Space_Shuttle_Speed = 0
        if event.key == pygame.K_a:
            x_Space_Shuttle_Speed = 0
        if event.key == pygame.K_w:
            y_Space_Shuttle_Speed = 0
        if event.key == pygame.K_s:
            y_Space_Shuttle_Speed = 0
        if event.key == pygame.K_SPACE:
            x_Shot += 8
            pygame.draw.circle(Background, yellow, (x_Space_Shuttle + 100 + x_Shot, y_Space_Shuttle + 15), 3)

    screen.fill(black)
    screen.blit(Background, (0, 50))
    screen.blit(Space_Shuttle, (x_Space_Shuttle, y_Space_Shuttle))
    pygame.display.flip()

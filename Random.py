import pygame

# Initialize the game engine
pygame.init()

# Display
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("SPACE INVADERS")
# Background
Background = pygame.image.load("Space.jpg")
Background = pygame.transform.scale(Background, (1400, 600))
# Colors
black = 0, 0, 0
yellow = 238, 201, 0

# Classes
class SpaceShuttle:
    def __init__(self, x, y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed

    def image(self):
        shuttleimg = pygame.image.load("Space_Shuttle.png")
        shuttleimg = pygame.transform.scale(shuttleimg, (100, 130))
        return shuttleimg


class Bullet:
    def __init__(self, x, xspeed):
        self.x = x
        self.xspeed = xspeed

    def image(self):
        Shot = pygame.draw.circle(Background, yellow, (Shuttle.x + 100 + self.x, Shuttle.y + 15), 3)
        return Shot


#Variables
Shuttle = SpaceShuttle(0, 300, 0, 0)
Bullet1 = Bullet(Shuttle.x, 0)

Running = False

while not Running:

    Shuttle.x += Shuttle.xspeed
    Shuttle.y += Shuttle.yspeed

    Bullet1.x += Bullet1.xspeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = True

        # Keys to move the space shuttle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            Shuttle.xspeed = 5
        elif event.key == pygame.K_a:
            Shuttle.xspeed = -5
        elif event.key == pygame.K_w:
            Shuttle.yspeed = -5
        elif event.key == pygame.K_s:
            Shuttle.yspeed = 5

        # Key to shoot bullets
        if event.key == pygame.K_SPACE:
            Bullet1.xspeed = 5
            old = Shuttle.x

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            Shuttle.xspeed = 0
        elif event.key == pygame.K_a:
            Shuttle.xspeed = 0
        elif event.key == pygame.K_w:
            Shuttle.yspeed = 0
        elif event.key == pygame.K_s:
            Shuttle.yspeed = 0

        # Key to shoot bullets
        if event.key == pygame.K_SPACE:
            Bullet1 = Bullet(old, 0)

    screen.fill(black)
    screen.blit(Background, (0, 50))
    screen.blit(Shuttle.image(), (Shuttle.x, Shuttle.y))

    Bullet1.image()
    pygame.display.flip()

''''
    # Collision circle with blocks                      # Collision Class
    if player1.x > (block1.x - 30) and player1.x < (block1.x + block1.width + 25) and player1.y > (block1.y - 31):
        player1.y = y_old
    if player1.x > (block1.x - 31) and player1.x < (block1.x + block1.width + 26) and player1.y > (block1.y - 30):
        player1.x = x_old
        
    self.x2 = x + width
        self.y2 = y - height

    linksboven = (self.x, self.y)
    rechtsonder = ((self.x + self.width)(self.y - self.height))
'''

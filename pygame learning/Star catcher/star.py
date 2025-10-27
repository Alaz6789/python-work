import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 500

background = pygame.image.load(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\Galaxy pic.jpg")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
pygame.display.set_caption("Star catcher")

class Bat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pass

    def update(self):
        pass

class Ball(pygame.sprite.Sprite):   # Inherit from Sprite
    def __init__(self, x, y):
        super().__init__()          # Call parent (Sprite) constructor
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 20)
        self.image.set_alpha(255) # 0-255, 0:invisible, 255:solid
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 1   # Moves the ball down every frame

ball_group = pygame.sprite.Group()
bat_group = pygame.sprite.Group()

ball_group.add(Ball(200, 10))
ball_group.add(Ball(300, 50))
#bat_group.add(Bat(250, 480))



clock = pygame.time.Clock()

runningstatus = True

BALLx = random.randint(1, 500)
BALLy = 15

BASKETx = 10
BASKETy = 480

BASKET_COLOUR = (255,255,255)
BALL_COLOUR = (255,0,0)

while runningstatus:
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, BASKET_COLOUR,(BASKETx, BASKETy, 100, 20))
    pygame.draw.circle(screen, BALL_COLOUR, (BALLx, BALLy), 10)
    pygame.display.update()

    BALLy += 1

    ball_group.update() 
    bat_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningstatus = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                print("right arrow button was clicked")
                BASKETx += 10

            if event.key == pygame.K_LEFT:
                print("left arrow was clicked")
                BASKETx -= 10

    clock.tick(60)

pygame.quit()
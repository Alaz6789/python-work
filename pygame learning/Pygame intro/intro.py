import pygame
import time

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

runningstatus = True

BACKGROUND_COLOUR = (57, 128, 227)
BALL_COLOUR = (207, 219, 234)

BALL_x = 250
BALL_y = 250

clock = pygame.time.Clock()

while runningstatus:

    clock.tick(60)

    screen.fill(BACKGROUND_COLOUR)

    pygame.draw.circle(screen, BALL_COLOUR, (BALL_x, BALL_y), 20)

    pygame.display.update()

    print(pygame.event.get())

    time.sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            runningstatus = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                print("UP arrow button was clicked")
                BALL_y -= 10

            if event.key == pygame.K_DOWN:
                print("down arrow button was clicked")
                BALL_y += 10

            if event.key == pygame.K_RIGHT:
                print("right arrow button was clicked")
                BALL_x += 10

            if event.key == pygame.K_LEFT:
                print("left arrow was clicked")
                BALL_x -= 10

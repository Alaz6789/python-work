import pygame

pygame.init()
clock = pygame.time.Clock
WIDTH, HEIGHT = 800, 600
background = pygame.image.load(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\Transforms\universeBG2.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.display.set_caption("Spin")

runningstatus = True

while runningstatus:
    screen.blit(background, (0,0))
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runningstatus = False
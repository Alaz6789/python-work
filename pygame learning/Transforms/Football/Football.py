import pygame

pygame.init()
clock = pygame.time.Clock()


WIDTH, HEIGHT = 800, 500
background = pygame.image.load(r"Transforms\Football\ftgr.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pygame.display.set_caption("Football")

class Football(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Transforms\Football\football.png")
        self.rect = self.image.get_rect(center = (400, 250))

    def update(self):
        pass

ball_group = pygame.sprite.Group()

runningstatus = True

while runningstatus:
    screen.blit(background, (0,0))
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runningstatus = False

    clock.tick(60)

pygame.quit()

        
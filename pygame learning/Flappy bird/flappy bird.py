import pygame
pygame.init()
screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy bird game")
bg = pygame.image.load(r"Flappy bird\bg.png")
ground = pygame.image.load(r"Flappy bird\ground.png")

class Flappybird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        for i in range(3):
            loadedImage = pygame.image.load(f"Flappy bird/bird{i+1}.png")
            self.images.append(loadedImage)
        self.countIndex = 0
        self.wait = 0
        self.image = self.images[self.countIndex]
        self.rect = self.image.get_rect(center = (100,screen_height//2))

    def update(self):
        self.wait += 1
        if self.wait > 10:
            self.wait = 0
            self.countIndex = (self.countIndex + 1)%len(self.images)
        self.image = self.images[self.countIndex]

bird = Flappybird()
sprite_group = pygame.sprite.Group()
sprite_group.add(bird)

groundmove = 0
if groundmove < -20:
    groundmove = 0

runningstatus = True

while runningstatus:
    screen.blit(bg,(0,0))
    screen.blit(ground, (groundmove, 740))
    sprite_group.draw(screen)
    sprite_group.update()
    groundmove -= 1
    if groundmove < -45:
        groundmove = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningstatus = False
    pygame.display.update()

pygame.quit()
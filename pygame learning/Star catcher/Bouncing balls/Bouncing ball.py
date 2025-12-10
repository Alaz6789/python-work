import pygame
import random


pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing balls")


# class to represent Ball, with extra game features 
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(15, 30)
        self.image = pygame.image.load(random.choice([(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\yb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\rb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\gb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\bb_.png")]))
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius)) 
        self.rect = self.image.get_rect(center=(random.randint(50,750), random.randint(50, 550)))
        self.x = self.rect.x
        self.y = self.rect.y
        self.speedx = random.randint(1,4)
        self.speedy = random.randint(1,4)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x < 20 or self.rect.x > 780:
            self.speedx = -self.speedx
            self.change_colour()

        if self.rect.y < 20 or self.rect.y > 580:
            self.speedy = -self.speedy
            self.change_colour()

    def change_colour(self):
        self.image = pygame.image.load(random.choice([(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\yb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\rb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\gb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\bb_.png")]))
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius)) 

    def reset(self):
        self.image = pygame.image.load(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\bb_.png")
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
        self.speedx = random.choice([-1,1])
        self.speedy = random.choice([-1,1])

    def start(self):
        self.speedx = random.randint(1,4)
        self.speedy = random.randint(1,4)

    def pause(self):
        self.speedx = 0
        self.speedy = 0


ball_group = pygame.sprite.Group()

amount_of_balls = 10
balls = [ball_group.add(Ball()) for ball in range(amount_of_balls)]


runningstatus = True

while runningstatus:
    screen.fill("skyblue")
    ball_group.draw(screen)
    ball_group.update()
    # ur gpu is gen frames each micro.mili sec, and giving to ur pygame window, if u dont update display it will kepp
    # showing the earlier frame that was generated first
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningstatus = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                for ball in ball_group:
                    if ball.speedx < 0 and ball.speedx != 1 and ball.speedx != -1:
                        ball.speedx += 1
                    if ball.speedx > 0 and ball.speedx != 1 and ball.speedx != -1:
                        ball.speedx -= 1

                    if ball.speedy < 0 and ball.speedy != 1 and ball.speedy != -1:
                        ball.speedy += 1
                    if ball.speedy > 0 and ball.speedy != 1 and ball.speedy != -1:
                        ball.speedy -= 1
            
            if event.key == pygame.K_RIGHT:
                for ball in ball_group:
                    if ball.speedx < 0 :
                        ball.speedx -= 1
                    if ball.speedx > 0 :
                        ball.speedx += 1

                    if ball.speedy < 0 :
                        ball.speedy -= 1
                    if ball.speedy > 0 :
                        ball.speedy += 1

            if event.key == pygame.K_SPACE:
                for ball in ball_group:
                    ball.reset()

            if event.key == pygame.K_UP:
                for ball in ball_group:
                    ball.start()

            if event.key == pygame.K_DOWN:
                for ball in ball_group:
                    ball.pause()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == pygame.BUTTON_LEFT or event.button == pygame.BUTTON_RIGHT:
                ball = Ball()
                ball_group.add(ball)

    clock.tick(60)



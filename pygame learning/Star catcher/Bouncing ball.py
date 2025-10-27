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
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.radius = random.randint(15, 30)
        self.dx = random.choice([-4, -3, 3, 4])
        self.dy = random.choice([-4, -3, 3, 4])

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.dy = -self.dy
    
    def draw(self):
        # image,rect,update()
        self.image = pygame.image.load(random.choice([(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\yb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\rb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\gb_.png"),(r"C:\Users\Alif Azhar\OneDrive - Colchester Royal Grammar School\Desktop\Documents\Dell Mama Backup 18.05.25\Alif's things\python code\pygame learning\bb_.png")]))
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius)) 
        self.rect = self.image.get_rect(center=(self.x,self.y))

amount_of_balls = 10
balls = [Ball() for ball in range(amount_of_balls)]

ball_group = pygame.sprite.Group()

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
                if ball.dx < 0:
                    ball.dx += 1
                if ball.dx > 0:
                    ball.dx -= 1

                if ball.dy < 0:
                    ball.dy += 1
                if ball.dy > 0:
                    ball.dy -= 1
            
            if event.key == pygame.K_RIGHT:
                if ball.dx < 0:
                    ball.dx -= 1
                if ball.dx > 0:
                    ball.dx += 1

                if ball.dy < 0:
                    ball.dy -= 1
                if ball.dy > 0:
                    ball.dy += 1

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == pygame.BUTTON_LEFT or event.button == pygame.BUTTON_RIGHT:
                #amount_of_balls += 1
                #balls = [Ball() for ball in range(amount_of_balls)]
                ball = Ball()
                ball.update()
                ball.draw()
                ball_group.add(ball)
    
    for ball in balls:
        ball.update()
        ball.draw()
        ball_group.add(ball)

    clock.tick(60)



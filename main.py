import pygame
import sys
import random

pygame.init()

# Set screen, caption, and background colour
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pong")
screen.fill((0, 0, 0))

score1 = 0
score2 = 0

text_font = pygame.font.SysFont("Arial", 40)

bounce = pygame.mixer.Sound("bouncewav.wav")
exit = pygame.mixer.Sound("wrong-47985.mp3")
exit.set_volume(0.3)
winning = pygame.mixer.Sound("win.mp3")
lose = pygame.mixer.Sound("defeat.mp3")
winning.set_volume(0.1)
lose.set_volume(0.1)


def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x, y))


# Draw boundary
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(499, 0, 2, 600))

# Player 1
player1Y = 200
player1temp = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, player1Y, 10, 150))

player1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, player1Y, 10, 150))

# Player Speed
player_speed = 0.8

# Ball
ballX = 500
ballY = random.randint(10, 590)
ballXspeed = random.choice([0.8, -0.8])
ballYspeed = random.uniform(0.4, -0.4)

# Player 2
player2Y = 200
player2temp = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(980, player2Y, 10, 150))

player2 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(980, player2Y, 10, 150))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(499, 0, 2, 600))

    # Ball movement
    ballcover = pygame.draw.circle(screen, (0, 0, 0), [ballX, ballY], 6)
    ballX += ballXspeed
    ballY += ballYspeed
    ball = pygame.draw.circle(screen, (255, 255, 255), [ballX, ballY], 6)

    # Ball boundary
    if ballY <= 0 or ballY >= 600:
        ballYspeed = ballYspeed * -1
    if ballX <= 10:
        ballcover = pygame.draw.circle(screen, (0, 0, 0), [ballX, ballY], 6)
        ballX = 500
        ballXspeed = random.choice([0.8, -0.8])
        ballYspeed = random.uniform(0.4, -0.4)
        score2 += 1
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 15, 50, 40))
        exit.play()
    if ballX >= 990:
        ballcover = pygame.draw.circle(screen, (0, 0, 0), [ballX, ballY], 6)
        ballX = 500
        ballXspeed = random.choice([0.8, -0.8])
        ballYspeed = random.uniform(0.4, -0.4)
        score1 += 1
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 15, 50, 40))
        exit.play()

    x = True
    # Checking for collision
    collide = ball.colliderect(player1)
    if collide:
        ballXspeed = ballXspeed * -1.1
        while x:
            score1 += 1
            x = False
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 15, 50, 40))
        bounce.play()
    collide2 = ball.colliderect(player2)
    if collide2:
        ballXspeed = ballXspeed * -1.1
        while x:
            score2 += 1
            x = False
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 15, 50, 40))
        bounce.play()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player1Y >= 10:
        player1temp = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, player1Y, 10, 150))
        player1Y -= player_speed
        player1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, player1Y, 10, 150))

    if keys[pygame.K_DOWN] and player1Y <= 440:
        player1temp = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, player1Y, 10, 150))
        player1Y += player_speed
        player1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, player1Y, 10, 150))

    player2temp = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(980, player2Y, 10, 150))

    player2Y_speed = player2Y - ballY + 60

    if player2Y_speed > 0:
        player2Y -= random.uniform(0.8, -0.3)
    else:
        player2Y += random.uniform(0.8, -0.3)

    player2 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(980, player2Y, 10, 150))

    if player2Y <= 10:
        player2Y = 10
    if player2Y >= 440:
        player2Y = 440

    draw_text(f"{score1}", text_font, (255, 255, 255), 200, 15)
    draw_text(f"{score2}", text_font, (255, 255, 255), 800, 15)

    if score1 >= 25:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1000, 600))
        draw_text("You win!", text_font, (255, 255, 255), 460, 280)
        bounce.stop()
        exit.stop()
        winning.play()

    elif score2 >= 25:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1000, 600))
        draw_text("You lose!", text_font, (255, 255, 255), 460, 280)
        bounce.stop()
        exit.stop()
        lose.play()


    pygame.display.update()

pygame.quit()
sys.exit()

import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shooting Game")
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 50     # target_img.get_width()
target_height = 50    # target_img.get_height()
dbl_target_width = 2 * target_width
dbl_target_height = 2 * target_height

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
count_color = (255,255,255)   #  random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
font = pygame.font.SysFont('courier new', 30)

running = True
dollars = 0
while running:
    screen.fill(color)
    drift = pygame.time.Clock().tick(300)
    target_x += random.randint(-drift, drift)
    target_y += random.randint(-drift, drift)
    if target_x <= 0:
        target_x = 0
    elif target_x + dbl_target_width >= SCREEN_WIDTH:
        target_x = SCREEN_HEIGHT - target_width
    if target_y <= 0:
        target_y = 0
    elif target_y + dbl_target_height >= SCREEN_HEIGHT:
        target_y = SCREEN_HEIGHT - target_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if target_x <= event.pos[0] <= target_x + target_width and target_y <= event.pos[1] <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (color[0] + drift, color[1] + drift, color[2] - drift)
                if int(color[0]) > 255:
                    color = (127, color[1], color[2])
                if int(color[1]) > 255:
                    color = (color[0], 127, color[2])
                if int(color[2]) < 0:
                    color = (color[0], color[1], 127)
                dollars += 1

    screen.blit(target_img, (target_x, target_y))
    message = "Dollars: " + str(dollars)
    text = font.render(message, True, count_color)
    screen.blit(text, (50, SCREEN_HEIGHT - 50))
    pygame.display.update()

pygame.quit()
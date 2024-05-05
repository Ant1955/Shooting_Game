import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Shooting Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('target.png')
target_width = 50     # target_img.get_width()
target_height = 50    # target_img.get_height()

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if target_x <= event.pos[0] <= target_x + target_width and target_y <= event.pos[1] <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
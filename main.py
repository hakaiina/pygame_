import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вращение спрайта")

sprite_image = pygame.image.load("monica.png").convert_alpha()

sprite_rect = sprite_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle = (angle + 1) % 360
    rotated_image = pygame.transform.rotate(sprite_image, angle)

    rotated_rect = rotated_image.get_rect(center=sprite_rect.center)

    screen.fill((255, 255, 255))

    screen.blit(rotated_image, rotated_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)


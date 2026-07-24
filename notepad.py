import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255,255,255)

screan = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NotePad")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screan.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
import pygame


# dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Object shadows')
screen.fill(WHITE)

object = pygame.Rect(((SCREEN_WIDTH // 2) - 25, (SCREEN_HEIGHT // 2) - 25), (50,50))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(surface=screen, color=BLACK, rect=object)

    pygame.display.update()


pygame.quit()
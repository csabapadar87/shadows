import pygame
from objects import Planet
import constants as const


pygame.init()

screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
pygame.display.set_caption('Object shadows')
screen.fill(const.WHITE)

object = pygame.Rect(((const.SCREEN_WIDTH // 2) - 25, (const.SCREEN_HEIGHT // 2) - 25), (50,50))
sun = Planet(surface=screen, rad=15, color=const.YELLOW, width=0)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                sun.set_pos(event.pos[0], event.pos[1])
                sun.draw()

    
    pygame.draw.rect(surface=screen, color=const.BLACK, rect=object)

    pygame.display.update()
    


pygame.quit()
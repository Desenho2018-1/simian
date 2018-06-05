
import pygame
class GameEngine(object):

    def __init__(self):
        pass

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 72)

    text = font.render("Hello, World", True, (0, 128, 0))
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False

        screen.fill((255, 255, 255))
        screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

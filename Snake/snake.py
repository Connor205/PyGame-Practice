import pygame
# import time
from pygame.locals import *
import os

pygame.init()

HEIGHT = 400
WIDTH = 600
FPS = 60

frames_per_second = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class 


class Player(pygame.sprite.Sprite):
    """
    Represents the player in the game 

    Args:
        pygame ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))


class Platform(pygame.sprite.Sprite):
    """
    Represents a platform in the game

    Args:
        pygame ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))


def main():
    """
    Runs the game from the main method
    """
    # Runs the main code
    pt_1 = Platform()
    p_1 = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(pt_1)
    all_sprites.add(p_1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape Pressed, exiting")
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
        displaysurface.fill((0, 0, 0))

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        pygame.display.update()
        frames_per_second.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()

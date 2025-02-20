import pygame

from constants import *
from utils import to_seconds
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Admin objects
    clock = pygame.time.Clock()
    dt = 0  # delta time

    # Game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()
        dt = to_seconds(clock.tick(60))
        

if __name__ == '__main__':
    main()

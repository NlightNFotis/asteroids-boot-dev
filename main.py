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
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)

    # Game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # for starters, update all objects (game state)
        updatables.update(dt)
        # paint background
        screen.fill('black')
        # paint objects on (top of) background
        for drawable in drawables:
            drawable.draw(screen)
        # clear screen
        pygame.display.flip()
        # calculate passed time since last draw
        dt = to_seconds(clock.tick(60))
        

if __name__ == '__main__':
    main()

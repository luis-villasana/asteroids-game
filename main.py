import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update game objects
        player.update(dt)

        # draw everythhing
        # first fill screen, then draw 
        # and then flip(update screen with what you've drawn)
        screen.fill("black")  
        player.draw(screen)
        pygame.display.flip()

        # control frame rate
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
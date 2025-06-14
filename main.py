import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    clock = pygame.time.Clock()

    # bucket(groups) that holds things that need to be updated every frame (moving, rotating,)
    updateable = pygame.sprite.Group()
    # bucket(group) that holds things that need to be drawn every frame (player, asteroids)
    drawable = pygame.sprite.Group()
    # group which will contain all the asteroids
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # defined before player initialization so that player obj automatically gets put into groups
    Player.containers = (updateable, drawable)
    # set containers field of Asteroid class to groups: asteroids, updateable, drawable
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # updates every obj in updatable group
        updateable.update(dt)

        for asteroid in asteroids:
            # collision check between asteroid and player
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
            # collision check between asteroid and bullets
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.kill()

        # draw everythhing
        # first fill screen, then draw 
        # and then flip(update screen with what you've drawn)
        screen.fill("black")          

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # control frame rate
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
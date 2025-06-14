import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        pygame.mixer.init()
        self.game_over = False
        self.score = 0

        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosionCrunch_000.ogg")

        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Player.containers = (self.updateable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidField.containers = (self.updateable)
        Shot.containers = (self.shots, self.updateable, self.drawable)

        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
    
    def run(self):
        dt = 0

        while True:
            # handle events
            self.handle_events()          
            self.update(dt)
            self.draw()
            # control frame rate
            # limit the framerate to 60 FPS
            dt = self.clock.tick(60) / 1000
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if self.game_over and event.type == pygame.KEYDOWN:
                self.restart()
    
    def update(self, dt):
        if self.game_over:
            return
    
        # updates every obj in updatable group
        self.updateable.update(dt)

        for asteroid in self.asteroids:
            # collision check between asteroid and player
            if asteroid.collides_with(self.player):
                self.game_over = True
                return
            
            # collision check between asteroid and bullets
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    self.explosion_sound.play()
                    points = asteroid.split()                    
                    if points:
                        self.score += points
    
    def draw(self):
         # draw everythhing
        # first fill screen, then draw 
        # and then flip(update screen with what you've drawn)
        self.screen.fill("black") 

        for obj in self.drawable:
            obj.draw(self.screen)

        score_surf = self.font.render(f"Score: {self.score}", True, "white")         
        self.screen.blit(score_surf, (10, 10))

        if self.game_over:
            msg = self.font.render("Game Over! Press any key to restart", True, "white")
            rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(msg, rect)

        pygame.display.flip()
    
    def restart(self):
        self.__init__()
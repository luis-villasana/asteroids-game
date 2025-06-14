import sys
import pygame
from constants import *
from game import Game
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    Game().run()

if __name__ == "__main__":
    main()
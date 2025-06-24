import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit(0)
            else:
                continue
        
        for obj in asteroids:
            for bullet in shots:
                if obj.collision_check(bullet):
                    obj.split()
                    bullet.kill()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
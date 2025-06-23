# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfields = pygame.sprite.Group()
    shotable = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shotable,updatable,drawable)

    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    run=True
    clock=pygame.time.Clock()
    dt=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for drw in drawable:
            drw.draw(screen)
        updatable.update(dt)


        for astr in asteroids:
            if astr.isCollision(player):
                print("Game over!")
                sys.exit()
            for bullets in shotable:
                if astr.isCollision(bullets):
                    bullets.kill()
                    astr.split()

        pygame.display.flip()
        dt=clock.tick(90)/1000



if __name__=="__main__":
    main()

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shots import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, drawable, updatable)

    Player.containers = (updatable, drawable)    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.check_collisions(player) == True:
                print("Game over!")
                exit()
            
            for shot in shots:
                if item.check_collisions(shot):
                    shot.kill()
                    item.split()

        for item in drawable:
            item.draw(screen)

        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
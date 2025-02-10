import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()

    pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    

    player = Player((SCREEN_WIDTH / 2), (SCREEN_WIDTH / 2), PLAYER_RADIUS)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for image in drawable:    
            image.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000
        

if __name__ == "__main__":
    main()
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        
        """
        bypassed declarations to directly change the triangle with .draw() instead of using built in methods.
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        """

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            Player.rotate(self, -dt)
        if keys[pygame.K_d]:
            Player.rotate(self, dt)
        if keys[pygame.K_s]:
            Player.move(self, -dt)
        if keys[pygame.K_w]:
            Player.move(self, dt)
        if keys[pygame.K_SPACE]:
            Player.shoot(self)

    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.add(self.containers)
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, object):
        """
        distance = self.position.distance_to(object.position)
        sum_of_radii = self.radius + object.radius
        print(f"Distance between objects: {distance}")
        print(f"Sum of radii: {sum_of_radii}")
        if (distance < sum_of_radii):
            return True
        return False
        """
        distance = self.position.distance_to(object.position)
        sum_of_radii = self.radius + object.radius
        return distance < sum_of_radii
        

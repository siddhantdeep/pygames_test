import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        v1=self.velocity.rotate(rand_angle)
        v2=self.velocity.rotate(-rand_angle)
        new_rad=self.radius-ASTEROID_MIN_RADIUS
        obj_1, obj_2 = Asteroid(self.position.x,self.position.y,new_rad),Asteroid(self.position.x,self.position.y,new_rad)
        obj_1.velocity = v1 * 1.2
        obj_2.velocity = v2 * 1.2
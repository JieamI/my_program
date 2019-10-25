import pygame
from pygame.locals import *


class wander_planet:
    def __init__(self):
        pygame.init()
        self.planet_img = pygame.image.load("planet_1.png")
        self.planet_rect = self.planet_img.get_rect().move(200,300)
        self.clock = pygame.time.Clock()                #返回时钟对象
        self.v = [0,1]
        self.temp_v = [0,0]
        self.speed = [0,0]
    
    def space_engine(self, m, rect):             #天体物理引擎
        self.clock.tick(50)
        r = ((rect.left - self.planet_rect.left)**2 + (rect.top - self.planet_rect.top)**2)**(1/2)
        self.a = (G * m)/(r**2)
        self.a_x = (rect.left - self.planet_rect.left) * self.a / r
        self.a_y = (rect.top - self.planet_rect.top) * self.a / r
        self.temp_v[0] = self.v[0]
        self.temp_v[1] = self.v[1]
        self.time = 5
        self.v[0] = self.v[0] + self.a_x * self.time
        self.v[1] = self.v[1] + self.a_y * self.time
        if self.a_x:
            self.speed[0] = (self.v[0]**2 - self.temp_v[0]**2)/(2 * self.a_x)
        else:
            self.speed[0] = self.v[0] * self.time
        if self.a_y:
            self.speed[1] = (self.v[1]**2 - self.temp_v[1]**2)/(2 * self.a_y)
        else:
            self.speed[1] = self.v[1] * self.time
        print(self.speed)
        
        
    def move(self):
        self.planet_rect = self.planet_rect.move(self.speed)
        screen.fill((0,0,0))
        screen.blit(self.planet_img, self.planet_rect)
        screen.blit(p_img, p_rect)
        pygame.display.flip()
        

if __name__ == '__main__':
    G = 1
    planet = wander_planet()
    screen = pygame.display.set_mode((800,600))
    p_img = pygame.image.load("planet_1.png")
    p_rect = p_img.get_rect().move(400,300)

    

    while True:
        planet.space_engine(200, p_rect)
        planet.move()

        
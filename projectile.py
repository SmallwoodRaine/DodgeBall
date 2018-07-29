from math import *


class Projectile:
    
    def __init__(self, x, y, initialVelocity):
        self.x = x
        self.y = y
        self.speed = 2
        self.velocity = initialVelocity
    
    def deflectBoundaries(self, wall):
        if self.x < wall.minX:
            self.velocity[0] *= -1
        if self.x > wall.maxX:
            self.velocity[0] *= -1
        if self.y < wall.minY:
            self.velocity[1] *= -1
        if self.y > wall.maxY:
            self.velocity[1] *= -1
        return self
    
    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        return self
    
    def setAngle(self, angle):
        self.velocity[0] = 3 * cos(angle)
        self.velocity[1] = 3 * sin(angle)
    
    def getAngle(self):
        return atan2(self.velocity[1], self.velocity[0])
    
    def collision(self, rock):
        xDiff = self.x - rock.x
        yDiff = self.y - rock.y
        theta = atan2(yDiff, xDiff)
        self.setAngle(2 * theta - self.getAngle())
        rock.setAngle(2 * theta - rock.getAngle())
        (self.velocity[0], rock.velocity[0]) = (
            rock.velocity[0], self.velocity[0])
        (self.velocity[1], rock.velocity[1]) = (
            rock.velocity[1], self.velocity[1])
        # projectiles sticking together fix
        angle = 0.5 * pi + theta
        self.x += sin(angle)
        self.y -= cos(angle)
        rock.x -= sin(angle)
        rock.y += cos(angle)
        return(self, rock)

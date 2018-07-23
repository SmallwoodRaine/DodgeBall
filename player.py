class Player:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
    
    def bounceBoundaries(self, wall):
        if self.x <= wall.minX:
            self.x += self.speed * 5
        if self.x >= wall.maxX:
            self.x -= self.speed * 5
        if self.y <= wall.minY:
            self.y += self.speed * 5
        if self.y >= wall.maxY:
            self.y -= self.speed * 5
        return self

import math

class JoyStick():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self, event):
        if (event.axis == 0):
            self.x = event.value
        elif (event.axis == 1):
            self.y = -event.value
        print(self.x, self.y)

    def get_polar_coords(self):
        r = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        theta = 0
        print(r)
        if (r > 0.5):
            theta = math.degrees(math.atan(self.x/self.y))
            if (self.x > 0 and self.y < 0):
                theta += 180
            elif (self.x < 0 and self.y < 0):
                theta += 180
            elif (self.x < 0 and self.y > 0):
                theta += 360
        


        return r, theta

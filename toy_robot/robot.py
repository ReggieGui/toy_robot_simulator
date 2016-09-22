from geography import Point,Direction

class Robot(object):
    
    def __init__(self,point,direction):
        self.point = point
        self.direction = direction
    
    def __repr__(self):
        return "{},{},{}".format(self.point.x,
                                 self.point.y,
                                 self.showOrientation())
    
    def moveTo(self,X,Y):
        self.point.x = X
        self.point.y = Y
    
    def rotateLeft(self):
        self.direction.leftDirection()
    
    def rotateRight(self):
        self.direction.rightDirection()
    
    def showOrientation(self):
        return self.direction.getOrientation()


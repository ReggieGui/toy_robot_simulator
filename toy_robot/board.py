from geography import *
from robot import Robot

class Board(object):
    """
    The tabletop to hosting the toy robot movement
    
    This object contains
    """
    robot = None
    step = 1
    DIFF_VECTOR = {
        "NORTH":[0,1*step],
        "WEST": [-1*step,0],
        "SOUTH":[0,-1*step],
        "EAST": [1*step,0]}

    def __init__(self,x=5,y=5):
        self.x=x  # length of the x axis
        self.y =y # length of the y axis
    def checkValid(self,newX,newY):
        """
        This function checks if x,y is inside the board
        """
        if 0 <= newX <=self.x and 0<=newY <=self.y:
            return True
        else:
            return False

    def place(self,x=0,y=0,orientation="NORTH"):
        try:
            x, y = int(x),int(y)
        except ValueError:
            # Hanlding invalid x and y axises
            return "--Please enter a valid integer"
        
        # Check if the position is inside the board
        if not self.checkValid(x,y):
            return "--The position is out of bounds"
        
        # Check if orientation is within the Direction dict
        if orientation.upper() not in Direction.DICTIONARY.values():
            return "--Unrecognised direction"
        
        # Place the robot accordingly
        self.robot = Robot(Point(x,y),Direction(orientation.upper()))

    def move(self):
        if self.robot == None:
            return "--No action!Robot is not on the table"
        
        # Create a new point array adding current vector and direction vector
        newPointArray = [v1 + v2 \
                         for v1, v2 in \
                         zip([self.robot.point.x,self.robot.point.y],\
                             self.DIFF_VECTOR.get(self.robot.showOrientation()))]
        # Check if the new point is inside the board
        if not self.checkValid(newPointArray[0],newPointArray[1]):
            return "--Next move is out of bounds"
        # Move the robot with a valid point
        self.robot.moveTo(newPointArray[0],newPointArray[1])

    def left(self):
        if self.robot == None:
            return "--No action!Robot is not on the table"
        self.robot.rotateLeft()
    
    def right(self):
        if self.robot == None:
            return "--No action!Robot is not on the table"
        self.robot.rotateRight()
    
    def report(self):
        if self.robot ==None:
            return "--No action!Robot is not on the table"
        return self.robot
    
    def exit(self):
        self.robot = None
        raise SystemExit()

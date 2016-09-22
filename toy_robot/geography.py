class Direction(object):
    
    # Store <key, value> pairs in dict
    DICTIONARY = {1:"NORTH",2:"WEST", 3:"SOUTH",4:"EAST"}
    
    def __init__(self,orientation):
        # Get key with a known value
        self.orientationKey = self.DICTIONARY.keys()\
            [self.DICTIONARY.values().index(orientation)]

    # Reset orientation key to the left orientation key
    def leftDirection(self):
        self.orientationKey = self.orientationKey%len(self.DICTIONARY) +1
    
    # Reset orientation key to the right orientation key
    def rightDirection(self):
        self.orientationKey = self.orientationKey%(len(self.DICTIONARY)/2) +1
    
    # Return the value of orientation
    def getOrientation(self):
        return self.DICTIONARY.get(self.orientationKey)

class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        return "({},{})".format(self.x,self.y)

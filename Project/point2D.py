class Point2D:
    # multiple constructor
    def __init__(self, *args):

        if (len(args) == 1):
            self.x = args[0].x
            self.y = args[0].y
            self.distanceToGoal = 0.0
            self.fScore = 0.0
            self.gScore = 0.0
            self.parentNode = Point2D()

        if (len(args) == 2):
            self.x = args[0]
            self.y = args[1]
            self.distanceToGoal = 0.0
            self.fScore = 0.0
            self.gScore = 0.0
            self.parentNode = Point2D()
    # https: // www.geeksforgeeks.org/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python/

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getDistanceToGoal(self):
        return self.distanceToGoal

    def setDistanceToGoal(self, val):
        self.distanceToGoal = val

    def getFScore(self):
        return self.fScore

    def setFScore(self, val):
        self.fScore = val

    def getGScore(self):
        return self.gScore

    def setGScore(self, val):
        self.gScore = val

    def getParentNode(self):
        return self.parentNode

    def setParentNode(self, val):
        self.parentNode = val

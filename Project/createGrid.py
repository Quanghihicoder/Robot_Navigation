class Grid:
    # init grid
    def __init__(self, pos, wall):
        self.pos = pos
        self.isWall = wall
        self.paths = []

    # pos getter
    def getPos(self):
        return self.pos

    # isWall getter
    def getIsWall(self):
        return self.isWall

    # isWall setter
    def setIsWall(self, val):
        self.isWall = val

    # path getter
    def getPath(self):
        return self.paths

    # path setter
    def setPath(self, val):
        self.paths = val

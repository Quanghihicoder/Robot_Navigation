from Project.createGrid import Grid
from Project.point2D import Point2D
from Project.createPath import Path


# check if any point in array match with a point in the map
def returnMatch(x, i, j):
    for p in x:
        if p.getPos().getX() == i and p.getPos().getY() == j:
            return p


class Map:

    # Map constructor
    def __init__(self, coordinate, mapWall):
        self.width = coordinate[0]
        self.length = coordinate[1]
        self.wall = mapWall
        self.grids = []
        self.wallList = []
        self.drawMap()

    #  Draw map
    def drawMap(self):
        for i in range(0, self.width):
            for j in range(0, self.length):
                self.grids.append(Grid(Point2D(j, i), False))

        for i in range(0, len(self.wall)):
            self.drawWall(self.wall[i])

        self.drawPath()

    def drawPath(self):
        for i in range(0, len(self.grids)):
            if (self.grids[i].getIsWall() == False):
                for j in range(0, self.width):
                    if ((i >= j * self.length) and (i < (j+1) * self.length - 1)):
                        self.grids[i].getPath().append(
                            Path(self.grids[i+1]))

                if (i < self.length * self.width - self.length):
                    if (self.grids[i+self.length].getIsWall() == False):
                        self.grids[i].getPath().append(
                            Path(self.grids[i+self.length]))

                for j in range(0, self.width):
                    if ((i > j * self.length) and (i < (j+1) * self.length)):
                        self.grids[i].getPath().append(
                            Path(self.grids[i-1]))

                if (i > self.length - 1):
                    if (self.grids[i - self.length].getIsWall() == False):
                        self.grids[i].getPath().append(
                            Path(self.grids[i-self.length]))

        for g in self.grids:
            # when the array remove a element, we need to loop again, otherwise the error: "index out of range" will happen
            i = 0
            while i < len(g.getPath()):
                if (g.getPath()[i].getLocation().getIsWall() == True):
                    g.getPath().remove(g.getPath()[i])
                    i = 0
                    break
                i += 1

    def drawWall(self, coordinate):
        for j in range(coordinate[1], coordinate[1]+coordinate[3]):
            for i in range(coordinate[0], coordinate[0]+coordinate[2]):
                index = self.grids.index(returnMatch(self.grids, i, j))
                self.grids[index].setIsWall(True)

        for g in self.grids:
            if(g.getIsWall() == True):
                self.wallList.append(g)

    def getGrids(self):
        return self.grids

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length

    def getWallList(self):
        return self.wallList

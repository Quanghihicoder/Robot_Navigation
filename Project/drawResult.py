import os


# check if any point in array match with a point in the map
def Any(x, i, j):
    for p in x:
        if (p.getX() == j and p.getY() == i):
            return p


# draw the searching process
def drawProcess(init, goal, wall, visitedNode, mapWidth, mapLength):
    os.system('cls')  # clear the console
    wallDrawn = False
    goalDrawn = False

    for i in range(0, mapWidth):
        for j in range(0, mapLength):
            if (init.getX() == j and init.getY() == i):
                print("|i", end='')
                continue

            for g in goal:
                if (g.getX() == j and g.getY() == i):
                    print("|g", end='')
                    goalDrawn = True
                    break
                goalDrawn = False

            if ((visitedNode.getX() == j) and (visitedNode.getY() == i) and goalDrawn == False):
                print("|x", end='')
                continue

            for w in wall:
                if(w.getIsWall() == True and w.getPos().getX() == j and w.getPos().getY() == i):
                    print("|w", end='')
                    wallDrawn = True
                    break
                wallDrawn = False

            if (wallDrawn == False and goalDrawn == False):
                print("| ", end='')
        print("|")


# draw the complete path
def drawCompletePath(init, goal, wall, path, mapWidth, mapLength):
    os.system('cls')  # clear the console
    wallDrawn = False
    goalDrawn = False

    for i in range(0, mapWidth):
        for j in range(0, mapLength):
            if (init.getX() == j and init.getY() == i):
                print("|i", end='')
                continue

            for g in goal:
                if (g.getX() == j and g.getY() == i):
                    print("|g", end='')
                    goalDrawn = True
                    break
                goalDrawn = False

            if (Any(path, i, j) and goalDrawn == False):
                print("|x", end='')
                continue

            for w in wall:
                if(w.getIsWall() == True and w.getPos().getX() == j and w.getPos().getY() == i):
                    print("|w", end='')
                    wallDrawn = True
                    break
                wallDrawn = False

            if (wallDrawn == False and goalDrawn == False):
                print("| ", end='')
        print("|")

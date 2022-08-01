class InitRes:
    def __init__(self, path):
        self.mapStructure = []
        self.initialState = []
        self.goalState = []
        self.wall = []
        self.path = path

    def populateData(self):
        file = open(self.path, "r")

        temp = []
        temp1 = []

        for index, lineVal in enumerate(file):
            if (index == 0):
                temp.append(lineVal.strip(
                    '\n').replace("[", "").replace("]", ""))
                for e in temp:
                    for s in e.split(","):
                        if (s.isdigit()):
                            self.mapStructure.append(int(s))
                temp = []

            if (index == 1):
                temp.append(lineVal.strip(
                    '\n').replace("(", "").replace(")", ""))
                for e in temp:
                    for s in e.split(","):
                        if (s.isdigit()):
                            self.initialState.append(int(s))
                temp = []

            if (index == 2):
                for gs in lineVal.strip('\n').split(" | "):
                    temp.append(gs.replace("(", "").replace(")", ""))

                for e in temp:
                    for s in e.split(","):
                        if (s.isdigit()):
                            temp1.append(int(s))
                    self.goalState.append(temp1)
                    temp1 = []
                temp = []

            if (index >= 3):
                temp.append(lineVal.strip('\n').replace(
                    "(", "").replace(")", ""))
                for e in temp:
                    for s in e.split(","):
                        if (s.isdigit()):
                            temp1.append(int(s))
                    self.wall.append(temp1)
                    temp1 = []
                temp = []

        file.close()

    def getMapStructure(self):
        return self.mapStructure

    def getInitialState(self):
        return self.initialState

    def getGoalState(self):
        return self.goalState

    def getWall(self):
        return self.wall

    def printInfo(self):
        print(self.mapStructure)
        print(self.initialState)
        print(self.goalState)
        print(self.wall)

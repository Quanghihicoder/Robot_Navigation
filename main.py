from Project.initMap import Map
from Project.readInputFile import InitRes
from Project.robot import robot
import sys

path = "RobotNav-test.txt"  # change to test


def main(argv):
    file = InitRes(path)
    file.populateData()

    map = Map(file.getMapStructure(), file.getWall())

    ai = robot(file.getInitialState(), file.getGoalState(), map)

    if(len(argv) == 0):
        print("Please give search method")
        print("There are 7 methods available: DFS, BFS, GBFS, AS, CUS1, CUS2, CUS3")
        print("Method CUS3 for the research section, not the origin problem")
        print("Example type in command: py main.py DFS")
    elif (len(argv) == 1):
        if argv[0] == "DFS":
            print(ai.DfsSearch())
        elif argv[0] == "BFS":
            print(ai.BfsSearch())
        elif argv[0] == "GBFS":
            print(ai.GbfsSearch())
        elif argv[0] == "AS":
            print(ai.AStarSearch())
        elif argv[0] == "CUS1":
            print(ai.UcsSearch())
        elif argv[0] == "CUS2":
            print(ai.IdasSearch())
        elif argv[0] == "CUS3":
            print(ai.VisitAllGoalShortest())
        else:
            print("Wrong format")
            print("There are 7 methods available: DFS, BFS, GBFS, AS, CUS1, CUS2, CUS3")
            print("Method CUS3 for the research section, not the origin problem")
            print("Example type in command: py main.py DFS")
    else:
        print("Wrong format")
        print("There are 7 methods available: DFS, BFS, GBFS, AS, CUS1, CUS2, CUS3")
        print("Method CUS3 for the research section, not the origin problem")
        print("Example type in command: py main.py DFS")

    # file.printInfo()


if __name__ == "__main__":
    main(sys.argv[1:])

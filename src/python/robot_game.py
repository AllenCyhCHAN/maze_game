from game_lib import *
import random

stateForTask4 = "findwall"
stateForTask6 = "findwall"

def makeDecisionForTask4():
    global stateForTask4

    if stateForTask4 == "findwall":
        if upIsWall():
            stateForTask4 = "Go left"
            return "NONE"
        else:
            return "UP"

    if stateForTask4 == "Go up":
        if not upIsWall() and rightIsWall():
            return "UP"
        if upIsWall() and rightIsWall():
            stateForTask4 = "Go left"
            return "NONE"
        elif not rightIsWall():
            stateForTask4 = "Go right"
            return "RIGHT"
        else:
            return "UP"

    elif stateForTask4 == "Go right":
        if not rightIsWall() and downIsWall():
            return "RIGHT"
        if downIsWall() and rightIsWall():
             stateForTask4 = "Go up"
             return "NONE"
        elif not downIsWall():
            stateForTask4 = "Go down"
            return "DOWN"
        else:
            return "RIGHT"
    elif stateForTask4 == "Go left":
        if not leftIsWall() and upIsWall():
            return "LEFT"
        if upIsWall() and leftIsWall():
            stateForTask4 = "Go down"
            return "NONE"
        elif not upIsWall():
            stateForTask4 = "Go up"
            return "UP"
        else:
            return "LEFT"
    elif stateForTask4 == "Go down":
        if not downIsWall() and leftIsWall():
            return "DOWN"
        if downIsWall() and leftIsWall():
            stateForTask4 = "Go right"
            return "NONE"
        elif not leftIsWall():
            stateForTask4 = "Go left"
            return "LEFT"
        else:
            return"DOWN"


def makeDecisionForTask6():
    global stateForTask6

    if getTotalNumberOfEnergyCells()!= getNumberOfCollectedEnergyCells():
        if leftIsExit():
            nono = "L"
        elif rightIsExit():
            nono = "R"
        elif upIsExit():
            nono = "U"
        elif downIsExit():
            nono = "D"
        else:
            nono = "Nothing"

    else:
        nono = "Nothing"
        
    if stateForTask6 == "findwall":
        if upIsWall() or nono == "U":
            stateForTask6 = "Go left"
            return "NONE"
        else:
            return "UP"

    if stateForTask6 == "Go up":
        if (not (upIsWall() or nono == "U")) and (rightIsWall() or nono == "R"):
            return "UP"
        if (upIsWall() or nono == "U") and (rightIsWall() or nono == "R"):
            stateForTask6 = "Go left"
            return "NONE"
        elif (not (rightIsWall() or nono == "R")):
            stateForTask6 = "Go right"
            return "RIGHT"
        else:
            return "UP"

    elif stateForTask6 == "Go right":
        if (not (rightIsWall() or nono == "R")) and (downIsWall() or nono == "D") :
            return "RIGHT"
        if (downIsWall() or nono == "D") and (rightIsWall() or nono == "R"):
             stateForTask6 = "Go up"
             return "NONE"
        elif (not (downIsWall() or nono == "D")):
            stateForTask6 = "Go down"
            return "DOWN"
        else:
            return "RIGHT"
    elif stateForTask6 == "Go left":
        if (not (leftIsWall() or nono == "L")) and (upIsWall() or nono == "U"):
            return "LEFT"
        if (upIsWall() or nono == "U") and (leftIsWall() or nono == "L"):
            stateForTask6 = "Go down"
            return "NONE"
        elif (not (upIsWall() or nono == "U")):
            stateForTask6 = "Go up"
            return "UP"
        else:
            return "LEFT"
    elif stateForTask6 == "Go down":
        if (not (downIsWall() or nono == "D")) and (leftIsWall() or nono == "L"):
            return "DOWN"
        if (downIsWall() or nono == "D") and (leftIsWall() or nono == "L"):
            stateForTask6 = "Go right"
            return "NONE"
        elif not (leftIsWall() or nono == "L"):
            stateForTask6 = "Go left"
            return "LEFT"
        else:
            return"DOWN"


chooseGameMap("task6", 0)


setDecisionFuncForTask4(makeDecisionForTask4)
setDecisionFuncForTask6(makeDecisionForTask6)

# Start the game
startGame()

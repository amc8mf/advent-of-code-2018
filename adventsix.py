import sys
sys.setrecursionlimit(10000)
# solution for error: "maximum recursion limit exceeded"

def getStartPoint(banksList, maxIndex):
    if maxIndex == len(banksList) - 1:
        return 0
    else:
        return maxIndex + 1

def countCycles(banksList, results=[], itrCount = 0):
    maxBank = max(banksList)
    maxIndex = banksList.index(maxBank)
    banksList[maxIndex] = 0
    isAtStartPoint = False
    endOfList = len(banksList) - 1
    startPoint = getStartPoint(banksList, maxIndex)
    x = 0
    while maxBank > 0:
        if isAtStartPoint == False:
            x = startPoint
            isAtStartPoint = True
        elif x == endOfList:
            banksList[x] += 1
            maxBank -= 1
            x = 0
        else:
            banksList[x] += 1
            maxBank -= 1
            x += 1
    itrCount += 1
    if results.count(banksList) < 2:
        results.append(list(banksList))
        countCycles(banksList, results, itrCount)
    else:
        # this part calculates the number of loops since the first occurrence of the repeated state
        #  (2nd part of Advent problem 6)
        results.append(list(banksList))
        firstIndex = results.index(banksList)
        results.remove(banksList)
        secondIndex = results.index(banksList)
        loopCount = (secondIndex + 1)  - firstIndex
        print(itrCount, loopCount)
#     originally had return itrCount, loopCount but that makes interpreter jump to line 34

countCycles([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])
# this gave a stack overflow error in pycharm, had to run code online to get answer

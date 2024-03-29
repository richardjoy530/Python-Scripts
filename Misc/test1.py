import time 
import numpy as np
ta = time.time() 

mainMatrix = np.random.randint(1,100, size=(100,100))
secondaryMatrix = np.random.randint(1,100, size=(40,5))
# mainMatrix = [[5, 6, 3, 4, 9, 3],
#               [9, 3, 5, 6, 1, 2],
#               [1, 2, 1, 4, 1, 7],
#               [3, 4, 9, 4, 1, 4],
#               [9, 3, 5, 6, 9, 3],
#               [1, 2, 7, 9, 1, 2]]

# secondaryMatrix = [[9, 3],
#                    [1, 2]]


MAIN_ROW = len(mainMatrix)
MAIN_COL = len(mainMatrix[0])
SEC_ROW = len(secondaryMatrix)
SEC_COL = len(secondaryMatrix[0])

# Section 1

checkStack = []
matchingIndex = []

for _, sec_row in enumerate(secondaryMatrix):
    matchingRowIndex = []

    for main_i, mainRow in enumerate(mainMatrix):
        checkStack = []
        # matchingRowIndex = []


        for main_j, element in enumerate(mainRow):

            # matching elements are inserted to a stack. and cleared once matching breaks
            # or the length becomes = SEC_COL
            if element == sec_row[len(checkStack)]:
                checkStack.append(element)
            else:
                checkStack = []

            if len(checkStack) == SEC_COL:
                matchingRowIndex.append([main_i, main_j-(SEC_COL-1)])
                checkStack = []
    # if len(matchingRowIndex) > 0:
    matchingIndex.append(matchingRowIndex)

# debug over here and see the matching indexes
# print(matchingIndex)

# Section 2

if SEC_ROW == 1:
    print("Succuss: ", matchingIndex[0])
else:
    count = 0
    for row in matchingIndex:
        for indexPair in row:
            for i in range(1,SEC_ROW):
                if [indexPair[0]+i, indexPair[1]] in matchingIndex[i]:
                    count = count+1
                else:
                    count = 0
                    break
                if count == SEC_ROW-1:
                    print('Succuss: ', indexPair)
                    count = 0
                    break

tb = time.time() 

print(tb-ta)
#  ----------In Section 1---------
# mainMatrix = [[5, 6, 3, 4, 7, 9],
#               [9, 3, 5, 6, 6, 7],
#               [1, 2, 1, 4, 1, 7],
#               [3, 4, 9, 4, 1, 4],
#               [3, 4, 5, 6, 9, 3],
#               [1, 2, 7, 9, 1, 2]]

# SecondaryMatrix = [[9, 3],
#                    [1, 2]]

# First we find occurance of all the rows and save it accordingly in a variable here it is "matchingIndex"

# In the given example, the matchingIndex = for row 1 of secondary matrix the occurance are in   [[1, 0], [4, 4],
#
#                                           for row 2 of secondary matrix the occurance are in   [2, 0], [5, 0], [5, 4]]

# Therefore here the matchingIndex is = [[1, 0], [4, 4],
#                                        [2, 0], [5, 0], [5, 4]]

#  ---------- In Section 2 ----------
# It is just a pattern matching logic.

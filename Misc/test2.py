import time 
import numpy as np
ta = time.time() 

# mainMatrix = np.random.randint(1,3, size=(500,500))
# secondaryMatrix = np.random.randint(1,3, size=(100,2))
mainMatrix = [[5, 6, 3, 4, 9, 3],
              [9, 3, 5, 6, 1, 2],
              [1, 2, 9, 4, 1, 7],
              [3, 4, 9, 4, 1, 4],
              [9, 3, 5, 6, 9, 3],
              [1, 2, 7, 9, 1, 2]]

secondaryMatrix = [[9, 4, 1],
                   [5, 6, 9]]

secondaryMatrixHash = []
mainMatrixHash = []

for row in secondaryMatrix:
    secondaryMatrixHash.append(hash(tuple(row)))


MAIN_ROW = len(mainMatrix)
MAIN_COL = len(mainMatrix[0])
SEC_ROW = len(secondaryMatrix)
SEC_COL = len(secondaryMatrix[0])

# Section 1

matchingIndex = []
matchingRowIndex = []

for main_i in range(len(mainMatrix)-SEC_ROW+1):
    rowHashMain = []
    for main_j in range(len(mainMatrix[0])-SEC_COL+1):
        sliced = mainMatrix[main_i][main_j:main_j+SEC_COL]
        rowHashMain.append(hash(tuple(sliced)))
    mainMatrixHash.append(rowHashMain)

for rowHash in secondaryMatrixHash:
    for i, row in enumerate(mainMatrixHash):
        for j, cellHash in enumerate(row):
            if rowHash == cellHash:
                matchingRowIndex.append([i, j])
    matchingIndex.append(matchingRowIndex)
    matchingRowIndex = []

# debug over here and see the matching indexes
print(matchingIndex)

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

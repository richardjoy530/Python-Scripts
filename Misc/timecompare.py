import time
import numpy as np

mainMatrix = np.random.randint(0,10, size=(30,30))
secondaryMatrix = np.random.randint(0,10, size=(2,2))

print(mainMatrix)
print("\n")
print(secondaryMatrix)
print("\n")

# mainMatrix = [[5, 6, 3, 4, 9, 3],
#               [9, 3, 5, 6, 1, 2],
#               [1, 2, 9, 4, 1, 7],
#               [3, 4, 9, 4, 1, 4],
#               [9, 3, 5, 6, 9, 3],
#               [1, 2, 7, 9, 1, 2]]

# secondaryMatrix = [[9, 4, 1],
#                    [5, 6, 9]]


def logic_1():
    ans = 0
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
        # print("Succuss: ", matchingIndex[0])
        ans = ans+1
    else:
        count = 0
        for row in matchingIndex:
            for indexPair in row:
                for i in range(1, SEC_ROW):
                    if [indexPair[0]+i, indexPair[1]] in matchingIndex[i]:
                        count = count+1
                    else:
                        count = 0
                        break
                    if count == SEC_ROW-1:
                        print("Match found at: ", indexPair)
                        ans = ans+1
                        count = 0
                        break
    print("logic_1 count: ", ans)


def logic_2():
    ans = 0
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
    for rowHash in secondaryMatrixHash:
        for main_i in range(len(mainMatrix)-SEC_ROW+1):
            for main_j in range(len(mainMatrix[0])-SEC_COL+1):
                sliced = mainMatrix[main_i][main_j:main_j+SEC_COL]
                if rowHash == hash(tuple(sliced)):
                    matchingRowIndex.append([main_i, main_j])
        matchingIndex.append(matchingRowIndex)
        matchingRowIndex = []

    # debug over here and see the matching indexes
    # print(matchingIndex)

    # Section 2

    if SEC_ROW == 1:
        ans = ans + 1
        # print("Succuss: ", matchingIndex[0])
    else:
        count = 0
        for row in matchingIndex:
            for indexPair in row:
                for i in range(1, SEC_ROW):
                    if [indexPair[0]+i, indexPair[1]] in matchingIndex[i]:
                        count = count+1
                    else:
                        count = 0
                        break
                    if count == SEC_ROW-1:
                        print("Match found at: ", indexPair)
                        ans = ans + 1
                        count = 0
                        break
    print("logic_2 count: ", ans)


def logic_3():
    ans = 0
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
    # print(matchingIndex)

    # Section 2

    if SEC_ROW == 1:
        # print("Succuss: ", matchingIndex[0])
        ans = ans+1
    else:
        count = 0
        for row in matchingIndex:
            for indexPair in row:
                for i in range(1, SEC_ROW):
                    if [indexPair[0]+i, indexPair[1]] in matchingIndex[i]:
                        count = count+1
                    else:
                        count = 0
                        break
                    if count == SEC_ROW-1:
                        print("Match found at: ", indexPair)
                        ans = ans+1
                        count = 0
                        break
    print("logic_3 count: ", ans)


def logic_4():
    MAIN_ROW = len(mainMatrix)
    MAIN_COL = len(mainMatrix[0])
    SEC_ROW = len(secondaryMatrix)
    SEC_COL = len(secondaryMatrix[0])
    SINGLE_MATCH = False

    count = 0

    si = 0  # secondaryMatrix Row
    sj = 0  # secondaryMatrix Col

    matchingStack = []

    # for index in range(MAIN_COL*MAIN_ROW):
    index = 0
    while index < MAIN_COL*MAIN_ROW:

        i = int(index/MAIN_ROW)  # mainMatrix Row
        j = index % MAIN_COL  # mainMatrix Col

        # print(mainMatrix[i][j])

        mainCell = mainMatrix[i][j]
        secondaryCell = secondaryMatrix[si][sj]

        if mainCell == secondaryCell:

            # Stop accepting once its a multiple of SEC_COL: False if matchingStack has multiple of SEC_COL
            condition1 = len(matchingStack) % SEC_COL != 0 or len(
                matchingStack) == 0

            # This condition is True if mainCell its below in the same column
            condition2 = False
            if len(matchingStack) != 0:
                condition2 = matchingStack[0][2] == j

            # This condition is for checking if its directly below. without any rows in between
            condition3 = False
            if len(matchingStack) >= SEC_COL:
                condition3 = matchingStack[-SEC_COL][1] == i-1
            
            # This is a edge case condition where matching continious from one row to the next without breaking 
            if len(matchingStack)!=0:
                if (not condition3) and condition1:
                    if matchingStack[len(matchingStack)-1][1] != i:
                        condition1 = False
                        
                        # resets index back to the first index of the matchingStack 
                        index = index - MAIN_COL*int(len(matchingStack)/SEC_COL) - len(matchingStack)%SEC_COL
                        matchingStack = []
                        si = 0
                        sj = 0

            if condition1 or (condition2 and condition3):
                matchingStack.append([mainMatrix[i][j], i, j])

                # A simple logic to use same loop for secondary matrix
                sj = sj + 1
                if sj == SEC_COL:
                    si = si+1
                    sj = 0
                if si == SEC_ROW:
                    print("Match found at: ", matchingStack[0][1:])
                    count = count + 1
                    si = 0
                    sj = 0

                    # Dont go back if the SEC_ROW is 1
                    if SEC_ROW > 1:
                        index = index - MAIN_COL*int(len(matchingStack)/SEC_COL) - SEC_COL + MAIN_COL + 1
                    matchingStack = []
                    if SINGLE_MATCH:
                        break
        else:
            # To erase if the elements in same are not matching
            condition4 = len(matchingStack) % SEC_COL != 0

            # To erase if elements in directly below row is not matching
            condition5 = False
            if len(matchingStack) >= SEC_COL:
                condition5 = matchingStack[-SEC_COL][1] == i - 1 and matchingStack[0][2] == j

            if condition4 or condition5:
                # Resets index back to the first index of the matchingStack 
                index = index - MAIN_COL*int(len(matchingStack)/SEC_COL) - len(matchingStack)%SEC_COL
                matchingStack = []
                si = 0
                sj = 0

        index = index + 1
    print("logic_4 count: ", count)



a = time.time()
logic_4()
b = time.time()
print("logic 4: ", b-a)
print("\n")

a = time.time()
logic_1()
b = time.time()
print("logic 1: ", b-a)
print("\n")

a = time.time()
logic_2()
b = time.time()
print("logic 2: ", b-a)
print("\n")

a = time.time()
logic_3()
b = time.time()
print("logic 3: ", b-a)
print("\n")


#   0   2   4   6   8   10  12  14  16  18 
# [[0 0 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 0 0 0]    0
#  [1 1 1 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1]    
#  [1 1 1 1 0 0 1 0 1 1 1 0 0 1 0 0 1 0 1 1]    2
#  [0 1 0 1 0 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1]
#  [0 1 1 1 0 1 0 0 0 0 0 1 0 0 1 1 1 1 1 0]    4
#  [0 0 1 0 0 1 1 0 0 0 0 0 1 1 1 0 1 1 1 0]
#  [1 1 0 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1]    6
#  [0 1 1 0 1 0 0 0 0 1 0 1 1 1 0 1 1 1 0 0]
#  [0 1 0 1 1 1 0 1 0 0 0 1 1 1 0 0 1 0 1 1]    8
#  [0 1 1 1 0 1 0 1 1 1 0 1 0 1 1 0 0 1 0 0]
#  [1 0 0 0 1 1 1 0 0 0 0 1 1 1 1 0 1 1 1 0]    10
#  [0 1 1 0 0 1 1 0 1 0 0 0 0 0 0 0 0 1 1 0]
#  [1 1 0 1 1 1 1 1 1 0 0 1 0 0 1 0 0 0 0 1]    12
#  [0 1 1 0 1 0 0 1 0 1 0 0 1 0 1 1 0 1 0 0]
#  [0 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 1 0]    14
#  [0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 1 0 0 1]
#  [1 0 1 1 0 1 0 0 0 1 0 1 1 1 0 1 1 0 0 0]    16
#  [1 1 1 1 0 1 0 0 0 1 1 0 1 0 1 0 0 1 0 0]
#  [0 0 1 0 1 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0]    18
#  [1 1 0 1 1 0 1 0 0 1 0 0 1 0 1 1 1 1 1 1]]   19
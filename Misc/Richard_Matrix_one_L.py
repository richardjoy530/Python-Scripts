import time
import numpy as np

ta = time.time()

mainMatrix = np.random.randint(0,2, size=(30,30))
secondaryMatrix = np.random.randint(0,2, size=(2,2))

print(mainMatrix)
print("\n")
print(secondaryMatrix)
print("\n")
# mainMatrix = [[9, 4, 3, 4, 9, 3],
#               [5, 6, 5, 6, 1, 2],
#               [1, 2, 9, 3, 1, 7],
#               [9, 3, 6, 6, 5, 6],
#               [1, 2, 7, 9, 1, 2]]

# secondaryMatrix = [[9, 4],
#                    [5, 6],
#                    [1, 2]]


# mainMatrix = [[0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
#               [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
#               [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
#               [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#               [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
#               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
#               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
#               [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
#               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
#               [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
#               [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
#               [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
#               [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
#               [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
#               [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
#               [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
#               [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#               [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#               [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
#               [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]]

# secondaryMatrix = [[0, 1, 0, 0, 0],
#                    [0, 1, 0, 0, 0],
#                    [0, 1, 0, 0, 0]]

MAIN_ROW = len(mainMatrix)
MAIN_COL = len(mainMatrix[0])
SEC_ROW = len(secondaryMatrix)
SEC_COL = len(secondaryMatrix[0])
SINGLE_MATCH = False

count = 0

si = 0  # secondaryMatrix Row
sj = 0  # secondaryMatrix Col

i = 0 # mainMatrix Row
j = -1 # mainMatrix Col

matchingStack = []

# for index in range(MAIN_COL*MAIN_ROW):
while True:

    # Calculating next index of the mainMatrix
    j = j + 1
    if j == MAIN_COL:
        i = i + 1
        j = 0
    
    if i == MAIN_ROW:
        break
    
    # print(mainMatrix[i][j])

    mainCell = mainMatrix[i][j]
    secondaryCell = secondaryMatrix[si][sj]

    if mainCell == secondaryCell:

        # Stop accepting once its a multiple of SEC_COL: False if matchingStack has multiple of SEC_COL
        condition1 = len(matchingStack) % SEC_COL != 0 or len(matchingStack) == 0

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

                    # Resets index back to the first index of the matchingStack
                    if len(matchingStack)!=0:
                        i = matchingStack[0][1]
                        j = matchingStack[0][2]

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

                    # Resets index back to the first index of the matchingStack
                    if len(matchingStack)!=0:
                        i = matchingStack[0][1]
                        j = matchingStack[0][2]

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
            if len(matchingStack)!=0:
                i = matchingStack[0][1]
                j = matchingStack[0][2]

            matchingStack = []
            si = 0
            sj = 0


tb = time.time()
# print(count)
print(tb-ta)

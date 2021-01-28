mainMatrix = [[5, 6, 3, 4, 7, 9],
              [9, 4, 5, 6, 6, 7],
              [3, 4, 1, 4, 1, 7],
              [3, 4, 9, 3, 6, 7],
              [3, 4, 5, 6, 6, 7],
              [1, 2, 7, 9, 1, 2]]

secondaryMatrix = [[1, 4],
                   [9, 3],
                   [5, 6]]


MAIN_ROW = len(mainMatrix)
MAIN_COL = len(mainMatrix[0])
SEC_ROW = len(secondaryMatrix)
SEC_COL = len(secondaryMatrix[0])

checkStack = []
matchingIndex = []

for sec_i in range(len(secondaryMatrix)):
    matchingRowIndex = []
    for main_i, mainRow in enumerate(mainMatrix):
        for main_j, rowElement in enumerate(mainRow):
            if rowElement == secondaryMatrix[sec_i][len(checkStack)]:
                checkStack.append(rowElement)
            else:
                checkStack = []
            if len(checkStack) == 2:
                matchingRowIndex.append([main_i, main_j-(SEC_COL-1)])
                checkStack = []
    if len(matchingRowIndex) > 0:
        matchingIndex.append(matchingRowIndex)

print(matchingIndex)




# maxOccurance = 0
# for row in matchingIndex:
#     if maxOccurance <= len(row):
#         maxOccurance = len(row)
# print(maxOccurance)

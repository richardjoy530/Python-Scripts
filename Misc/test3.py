mainMatrix = [[5, 6, 3, 4, 9, 3],
              [9, 3, 5, 6, 1, 2],
              [1, 2, 1, 4, 1, 7],
              [3, 4, 9, 4, 1, 4],
              [9, 3, 5, 6, 9, 3],
              [1, 2, 7, 9, 1, 2]]

secondaryMatrix = [[9, 3],
                   [1, 2]]

secondaryMatrixHash = []
mainMatrixHash = []

for row in secondaryMatrix:
    secondaryMatrixHash.append(hash(tuple(row)))

MAIN_ROW = len(mainMatrix)
MAIN_COL = len(mainMatrix[0])
SEC_ROW = len(secondaryMatrix)
SEC_COL = len(secondaryMatrix[0])

# Section 1

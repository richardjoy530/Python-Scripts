mainMatrix = [[5, 6, 3, 4, 9, 3],
              [9, 3, 5, 6, 1, 2],
              [1, 2, 1, 4, 1, 7],
              [3, 4, 9, 4, 1, 4],
              [9, 3, 5, 6, 9, 3],
              [1, 2, 7, 9, 1, 2]]

a= []

for i in mainMatrix:
    for j in i:
        a.append(j)

print(a)
        
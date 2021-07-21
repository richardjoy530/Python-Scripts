q = [2, 5, 1, 3, 4]
bribes = 0
i = 0
while True:
    # Terminate the loop
    if i == len(q):
        print(bribes)
        break

    stickerNumber = q[i]
    realPosition = i+1

    # print(stickerNumber, realPosition)
    if(stickerNumber-realPosition > 2):
        print("Too chaotic")
        break
    bribes += stickerNumber-realPosition
    q.remove(stickerNumber)
    q.insert(stickerNumber-1, stickerNumber)
    print(q)
    i += 1


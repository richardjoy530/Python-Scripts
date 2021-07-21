# N = int(input())
N = 1
for _ in range(N):
    # [A, B, n] = map(str, input().split())
    [A, B, n] = map(str, '14159265351234512342 8272323846 1'.split())
    # [A, B, n] = map(str, '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196 1000000000000000000000000000000'.split())
    n = int(n) - 1
    lA = len(A)
    lB = len(B)
    lastTermLength = 2
    perviouslastTermLengthLength = lA
    while True:
        lC = lA + lB
        perviouslastTermLengthLength = lB
        lastTermLength = lC
        if lC > n:
            break
        lA = lB
        lB = lC

    right = perviouslastTermLengthLength
    left = lastTermLength - perviouslastTermLengthLength
    whole = lastTermLength

    if n < len(A)+len(B):
        AB = A+B
        print(AB[n])
        continue

    while True:
        if n > left:
            n = n-left

        else:
            whole = right
            right = left
            left = whole - right

        whole = right
        right = left
        left = whole - right

        if whole == len(A)+len(B):
            AB = A+B
            print(AB[n])
            break
        if whole == len(B)+len(A)+len(B):
            BAB = B+A+B
            print(BAB[n])
            break

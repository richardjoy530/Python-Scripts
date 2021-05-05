# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for _ in range(N):
    [A, B, n] = map(str, input().split())
    n = int(n)
    n = n-1
    lA = len(A)
    lB = len(B)
    pA = 'A'
    pB = 'B'
    pattern = ''
    term = 2
    while True:
        lc = lA + lB
        # print(term)
        # pattern = pA+pB
        term += 1
        if lc >= n:
            print(term)
            break
        lA = lB
        # pA = pB
        lB = lc
        # pB = pattern

    # totalDigits = 0
    # for i in pattern:
    #     if i == 'A':
    #         totalDigits += len(A)
    #     else:
    #         totalDigits += len(B)

    #     if totalDigits >= n:
    #         if i == 'A':
    #             totalDigits -= len(A)
    #         else:
    #             totalDigits -= len(B)

    #         index = n - totalDigits
    #         if i == 'A':
    #             print(A[index])
    #         else:
    #             print(B[index])
    #         break


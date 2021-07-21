# N = int(input().strip())
N = 1
for _ in range(N):
    # n = int(input().strip())
    n = 100
    A = 1
    B = 2
    S = 2
    while True:
        C=A+B
        if C>=n:
            break
        A=B
        B=C
        if C%2==0:
            S+=C
    print(S)

        


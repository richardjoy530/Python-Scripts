t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int,input().split()))
    recordDay = 0
    big = 0
    for i,j in enumerate(v):
        if i<len(v)-1:
            if j>v[i+1] and big<j:
                big=j
                recordDay = recordDay + 1
        
        if big < j and i==len(v)-1:
            recordDay = recordDay + 1
    print('Case #1: ',recordDay)

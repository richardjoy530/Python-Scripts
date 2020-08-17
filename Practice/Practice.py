N = int(input())

array = []
for i in range(N):
    a = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    for j in range(a[1]):
        array.insert(0,array[a[0]-1])
        array.pop(a[0])

    print(' '.join(map(str, array)))

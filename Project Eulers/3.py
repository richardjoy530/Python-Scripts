# N = int(input().strip())
N = 1
for _ in range(N):
    # n = int(input().strip())
    n = 7919 
    number = n
    l = 1
    i=2
    while True:
        if n%i==0:
            n=int(n/i)
            if n<=l:
                print(i)
                break
            l=i
            i-=1
        i+=1
        if i > number/3:
            print(number)
            break
# N = int(input().strip())
N = 1
for _ in range(N):
    # n = int(input().strip())-1
    n = 1234567891 - 1 
    l3 = int(n/3)
    l5 = int(n/5)
    l15 = int(n/15)
    sum3 = l3>>1*(2*3+(l3-1)*3)
    sum5 = l5>>1*(2*5+(l5-1)*5)
    sum15 = l15>>1*(2*15+(l15-1)*15)

    print(int(sum3+sum5-sum15))

    # sum = 0
    # for i in range(1,n+1):
    #     if i%3==0 or i%5==0:
    #        sum+=i
    # print(sum)
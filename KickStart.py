rows = 5
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(0,i):
        print(b,end=' ')
    print('\r')
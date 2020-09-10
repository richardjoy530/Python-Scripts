c=0
for i in range(999996,12,-12):
    if(c!=4 and str(i)==str(i)[::-1] and len(set(str(i)))<=2):
        print(i)
        c=c+1
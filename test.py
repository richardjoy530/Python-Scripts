import itertools

twoDigits = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0],2))

threeDigits = []
for i in twoDigits:
    for firstDigit in i:
        for secondDigit in i:
            for thirdDigit in i:
                threeDigits.append((firstDigit,secondDigit,thirdDigit))

largest = [(0),(0),(0),(0)]

for i in threeDigits:
    temp = i[0]*100000+i[1]*10000+i[2]*1000+i[2]*100+i[1]*10+i[0]
    if temp%12==0 and temp not in largest:
        if temp >largest[0]:
            largest[0]=temp
        elif temp>largest[1]:
            largest[1]=temp
        elif temp>largest[2]:
            largest[2]=temp
        elif temp>largest[3]:
            largest[3]=temp

print(largest)
        



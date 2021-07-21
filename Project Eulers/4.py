import math
N = int(input().strip())
# N = 1
for _ in range(N):
    n = int(input().strip())
    # n = 800000
    # 800008 X    799 997
    (firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit, sixthDigit) = (int(n/100000),
                                                                                  int((n % 100000)/10000), int((n % 10000)/1000), int((n % 1000)/100), int((n % 100)/10), int(n % 10))

    if firstDigit*100000 + secondDigit*10000 + thirdDigit*1000 + thirdDigit*100 + secondDigit*10 + firstDigit < n:
        sectionOneMax = int(n/1000)
    else:
        sectionOneMax = int(n/1000)-1

    for sectionOne in range(sectionOneMax, 99, -1):

        (firstDigit, secondDigit, thirdDigit) = (int((sectionOne % 1000)/100),
                                                 int((sectionOne % 100)/10), int(sectionOne % 10))
        pallindrome = firstDigit*100000 + secondDigit*10000 + \
            thirdDigit*1000 + thirdDigit*100 + secondDigit*10 + firstDigit

        # print(pallindrome)
        found = False
        # getting 3 digit factors
        for i in range(101, 1000):
            if pallindrome % i == 0:
                factor = pallindrome/i
                # check if the factor is 3 digit
                if factor > 99 and factor < 1000:
                    found = True
                    print(pallindrome)
                    break
        if found:
            break
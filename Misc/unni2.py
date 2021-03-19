T = int(input())
for _ in range(T):
    arr = input()
    steps = 0
    q_count = 0
    max_count = 0
    for i in arr:
        if i == "A":
            steps = steps+1
        elif i == "C":
            steps = steps-1
        else:
            q_count = q_count+1
        
        if max_count < abs(steps+q_count):
            max_count = abs(steps+q_count)
        if max_count < abs(steps-q_count):
            max_count = abs(steps-q_count)
        
    print(max_count)

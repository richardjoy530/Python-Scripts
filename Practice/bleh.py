a = 'a'
b = 'b'
c= ''

for _ in range(10):
    c = a+b
    print(len(c), c,)
    a = b
    b = c
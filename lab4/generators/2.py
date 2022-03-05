def generators(n):
    for i in range(0,n+1,2):
        yield i

for i in generators(int(input())):
    print(i)
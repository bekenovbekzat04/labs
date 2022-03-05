def gen(n):
    for i in range(0,n+1,3):
        yield i
def gen1(n):
    for i in range(0,n+1,4):
        yield i
n= int(input())
for i,j in gen(n),gen1(n):
    print(i,j)


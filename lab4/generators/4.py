def gensquares(m,n):
    for i in range(m,n+1):
        yield i**2
a=list(map(int,input().split()))
for i in gensquares(a[0],a[1]):
    print(i)
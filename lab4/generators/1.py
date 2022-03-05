def gensquares(n):
    for i in range(n+1):
        yield i**2
for i in gensquares(int(input())):
    print(i)

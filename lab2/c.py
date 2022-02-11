b=int(input())
a=[[0 for i in range(b)] for j in range(b)]
for i in range(b):
    for j in range(b):
        if i==j:
            a[i][j]=i*j
        a[0][j]=j
        a[i][0]=i
for i in range(b):
    for j in range(b):
        print(a[i][j],end=" ")
    print()
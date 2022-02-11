a,b=[i for i in input().split()],[]
for i in range(len(a)):
    if len(a[i])>=3:
        b.append(a[i])
for i in range(len(b)):
    print(b[i], end=" ")
n=int(input())
if n%2==0:
    for i in range(1,n+1):
        for j in range(i):
            print('#',end='')
        for j in range(n-i):
            print('.',end='') 
        print(''' ''')
else:
    for i in range(1,n+1):
        for j in range(n-i):
            print('.',end='')
        for j in range(i):
            print('#',end='') 
        print(''' ''')
input()
s,a=input().split(),[]
for i in range(len(s)):
    a.append(int(s[i]))
a.sort()
print(int(a[len(a)-1])*int(a[len(a)-2]))
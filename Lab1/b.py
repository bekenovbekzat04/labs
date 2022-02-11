a,sum=input(),0
for i in range(len(a)):
    sum+=ord(a[i])
if(sum>300):
    print("it is tasty")
else:
    print("oh, no!")
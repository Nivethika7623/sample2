a1=int(input())
b1=int(input())
if(a1>b1):
    min1=a1
else:
    min1=b1
while(1):
    if(min1%a1==0 and min1%b1==0):
        print("LCM is:",min1)
        break
    min1=min1+1

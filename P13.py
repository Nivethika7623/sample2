x=int(input())
sum=0
while(x>0):
    dig=x%10
    sum=sum+(dig*dig)
    x=x//10
print(sum)

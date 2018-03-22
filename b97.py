n1=int(input())
rev1=0
while(n1>0):
    dig1=n1%10
    rev1=rev1*10+dig1
    n1=n1//10
print(rev1)

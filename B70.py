n=int(input())
c=0
x=1
p=2
while(n!=1):
   n=n/2
   c=c+1
for i in range(0,c+1):
    x=x*p
print(x)

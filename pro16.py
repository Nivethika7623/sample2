n1=int(input())
l=[]
a=0
for i in range(n1):
    a=int(input())
    l.append(a)
l.sort()
candy=0
c=0
for i in range(n1):
    candy=candy+l[i]
print(candy)

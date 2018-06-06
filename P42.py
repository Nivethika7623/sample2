a=int(input())
l=[]
c=[]
d=[]
for i in range(0,a):
    b=int(input())
    l.append(b)
    c.append(b)
l.sort()
print(c)
print(l)
if l==c:
    print("yes")
else:
    print("no")

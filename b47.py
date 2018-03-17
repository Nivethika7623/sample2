a1=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b1=int(input("Enter element:"))
    a1.append(b1)
a1.sort()
print(min(a1))
print(max(a1))

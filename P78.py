a1=[]
c1=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b1=int(input("Enter element:"))
    a1.append(b1)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d1=int(input("Enter element:"))
    c1.append(d1)
new=a1+c1
new.sort()
print("Sorted list is:",new)

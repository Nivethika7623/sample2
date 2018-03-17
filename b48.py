n1=int(input("Enter the number of elements to be inserted: "))
a1=[]
for i in range(0,n1):
    elem1=int(input("Enter element: "))
    a1.append(elem1)
avg1=sum(a1)/n11
print("Average of elements in the list",round(avg1,2))

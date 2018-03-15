a1=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
  b=int(input("Enter element:"))
  a1.append(b)
a1.sort()
print("Largest element is:",a1[n-1])

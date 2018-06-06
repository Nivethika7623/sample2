A=int(input("enter a number"))
B=int(input("enter a number"))
for i in range(2,1000):
    if A%i==0 and B%i==0:
        break
print(i)

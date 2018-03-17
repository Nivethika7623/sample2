n1=int(input("Enter a number:"))
tot1=0
while(n1>0):
    dig1=n1%10
    tot1=tot1+dig1**2
    n1=n1//10
print("The total sum of digits is:",tot1)

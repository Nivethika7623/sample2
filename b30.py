a=int(input("Enter the hour:"))
b=int(input("Enter the min:"))
c=int(input("Enter the hour1:"))
d=int(input("Enter the min1:"))
e=a*60+b
f=c*60+d
g=e-f
print(g//60,g%60)

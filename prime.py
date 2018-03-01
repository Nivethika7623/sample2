N=int(input("Enter number:"))
k=0
for i in range(2,N//2+1):
  if(a%i==0):
    k=k+1
if(k<=0):
  print(N,"is prime number")
else:
  print(N,"is not a prime number")

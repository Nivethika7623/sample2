n=int(input())
fact=1
if(n<=20):
  while(n>0):
    fact=fact*n
    n=n-1
  print("Factorial of the number is:")
  print(fact)
else:
  print("Please enter correct number")

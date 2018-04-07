temp=0
count=0
num=input("Enter the number: ")
while(num!=0):
		temp=num%10
		count=0
		if(temp==1 and temp==0):
			count=1
		else:
			break
		num=num/10
if(count==1):
		print("yes")
else:
    print("no")

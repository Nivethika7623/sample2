st=input()
vow=['a','e','i','o','u','A','E','I','O','U']
flag=0
for x in st:
	if x in vow:
		flag=1
if(flag==1):
	print("yes")
else:
	print("no")

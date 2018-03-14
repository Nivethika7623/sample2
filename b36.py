string1=str(input("Enter string:"))
count1=0
count2=0
for i in string1:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)

s1=['a','e','i','o','u']
a1=input("enter the string")
l1=[]
for i in range(len(a1)):
    if a1[i] not in s1:
        l1.append(a1[i])
b1=l1[::-1]
print(str(b1))

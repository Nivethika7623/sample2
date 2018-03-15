a=int(input())
b=int(input())
print("First value is ",a)
print("Second value is ",b)
a = a ^ b
b = a ^ b
a = a ^ b
print("== After Swapping ==")
print("First value is ",a)
print("Second value is ",b)

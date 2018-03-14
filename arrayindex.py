def reorder(arr, index, n):
for i in range(0,n):
           while (index[i] != i):
               oldTargetI = index[index[i]]
               oldTargetE = arr[index[i]]
               arr[index[i]] = arr[i]
               index[index[i]] = index[i]
               index[i] = oldTargetI
               arr[i] = oldTargetE
arr = [50, 40, 70, 60, 90]
index= [3, 0, 4, 1, 2]
n = len(arr)
reorder(arr, index, n)
print("Reordered array is:")
for  i in range(0, n):
    print(arr[i],end=" ") 
print("\nModified Index array is:")
for i in range(0, n):
    print(index[i] ,end=" ")

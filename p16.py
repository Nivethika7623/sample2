def firstNonRepeating(arr, n):
    for i in range(n): 
        j = 0
        while(j < n): 
            if (i != j and arr[i] == arr[j]): 
                break
            j += 1
        if (j == n): 
            return arr[i] 
      
    return -1
arr = list()
n = int(input())
for i in range(n):
    m =int(input())
    arr.append(m)
print(firstNonRepeating(arr, n))

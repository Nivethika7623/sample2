def findMean(a, n):
    sum = 0
    for i in range( 0, n):
        sum += a[i]
     
    return float(sum/n)
def findMedian(a, n):
    sorted(a)
    if n % 2 != 0:
        return float(a[n/2])
     
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0)
a = [ 2,3,1 ]
n = len(a)
print("Median =", findMedian(a, n))

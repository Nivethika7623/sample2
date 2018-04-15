def sqrt(x):
    ans = 0
    if x >= 0:
        while(ans*ans < x):
            ans = ans + 1
            if ans*ans != x:
                print(x, 'is not a perfect square.')
                return None
            else:
                print(x, ' is a perfect square.')
                return ans
    else:
        print(x, ' is not a positive number.')
        return None

y =int(input()) 
sqrt(y)

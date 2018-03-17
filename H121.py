def substrings(s):
    l = len(s)
    for end in range(l, 0, -1):
        for i in range(l-end+1):
            yield s[i: i+end]
def palindrome(s):
    return s == s[::-1]
def Question2(a):
    for l in substrings(a):
        if palindrome(l):
            return l
a1=str(input())
print(Question2(a1))

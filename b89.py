def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)
s1=input()
print(lexicographi_sort(s1))

str =int(input())
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNo')
print('Yes')

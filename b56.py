def count(x):
    length1 = len(x)
    digit1= 0
    letters1 = 0
    space1 = 0
    other1 = 0
    for i in x:
        if x[i].isalpha():
            letters1 += 1
        elif x[i].isnumeric():
            digit1 += 1
        elif x[i].isspace():
            space1 += 1
        else:
            other1 += 1
    return number1,word1,space1,other1

str1=str(input("Enter string:"))
char1=0
word1=1
for i in str1:
      char1=char1+1
      if(i==' '):
            word1=word1+1
print("Number of words in the string:")
print(word1)
print("Number of characters in the string:")
print(char1)

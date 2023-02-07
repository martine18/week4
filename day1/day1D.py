#Daily Challenge: Build Up A String

 answer= input("write a text:  ")
if(len(answer)<10):
    print("string is too long enought")
    
elif(len(answer) >10):
    print("string is too long")
firstChar = answer[0]
lastChar = answer[-1]

print(firstChar)
print(lastChar)

#section 3 
#Using a for loop, construct the string character by character: Print the first character,
# then the second, then the third, until the full string is printed. For example:

result= ""
for character in answer:
    result += character
    print( result)
    











#Daily Challenge: Build Up A String

input("enter 10 character of string")[:10]

while True:
    answer = input("string not long enogh")
    if len(answer) <= 10:
        break
    else:
        print("string is too long")
        
 
firstChar = answer[0]
lastChar = answer[-1]

print(firstChar)
print(lastChar)

#section 3 
#Using a for loop, construct the string character by character: Print the first character,
# then the second, then the third, until the full string is printed. For example:

input("user input :hello world")

for x in "hello world":
    print(x)
 











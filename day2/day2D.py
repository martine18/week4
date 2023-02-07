


num = int(input("Enter a number: "))
length = int(input("Enter a length: "))

result = []
for i in range(1, length+1):
    result.append(num * i)
print(result)

#Challenge 2


strValue = "ppoeemm"+ "\t" +"wiiiinnnnd"+ "\t" +"ttiiitllleeee"+  "\t" +"cccccaaarrrbbonnnnn"
strValue = ''.join(sorted(set(strValue), key=strValue.index))
print(strValue)







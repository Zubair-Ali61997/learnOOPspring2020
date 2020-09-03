#Taking the range of number from the user to find even and odd using for loop
startNum = int(input("Enter starting value: "))
endNum = int(input("Enter end value: "))
for eachNumber in range(startNum,endNum+1):
    modeValue = eachNumber % 2
    if modeValue == 0:
        print(eachNumber, "is an even")
    else:
        print(eachNumber, "is an odd")

#Taking the range of number from the user to find even and odd using while loop

# taking_a_value = int(input("Enter a value: "))
startNum = int(input("Enter starting value: "))
endNum = int(input("Enter end value: "))

while (startNum >= endNum):
    modeValue = endNum % 2
    if modeValue == 0:
        print(endNum, "is an even")
    else:
        print(endNum, "is an odd")
    endNum=endNum+1

#Finding totel number of odd and even in a range using for loop
startNum = int(input("Enter starting value: "))
endNum = int(input("Enter end value: "))
evenNumber = 0
oddNumber = 0
for eachNumber in range (startNum, endNum+1):
    modeValue = eachNumber % 2
    if modeValue == 0:
        evenNumber = evenNumber + 1
    else:
        oddNumber = oddNumber + 1
print ("Total number of even number is = ",evenNumber)
print ("Total number of odd number is = ",oddNumber)

# Finding totel number of odd and even in a range using while loop
startNum = int(input("Enter starting value: "))
endNum = int(input("Enter end value: "))
evenNumber = 0
oddNumber = 0
while (startNum >= endNum):
    modeValue = endNum % 2
    if modeValue== 0:
        evenNumber = evenNumber + 1
    else:
        oddNumber = oddNumber + 1

    endNum = endNum + 1
print ("Total number of even number is = ",evenNumber)
print ("Total number of odd number is = ",oddNumber)
#Table using while loop


table = int(input("Enter a number: "))
startNum = int(input("Enter a start number: "))
endNum = int(input("Enter a end number: "))
i = startNum
while (i <= endNum):
    print (i,"*",table,"=",i*table)
    i=i+1
print("#######################################################")
#Table using for loop

table = int(input("Enter a number: "))
startNum = int(input("Enter a start number: "))
endNUm = int(input("Enter a end number: "))
for foreachnumber in range(startNum, endNum+1):
    print (i,"*",table,"=",i*table)
print("########################################################")
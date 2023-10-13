
while True:
    try:
        binaryNum = int(input("Give me a binary number\n"))
        break
    except:
        print("Input a integer please")

decimalNum = int(str(binaryNum), 2)

print(binaryNum+" -> "+str(decimalNum))






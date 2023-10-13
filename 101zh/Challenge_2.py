
while True:
    try:
        originalNum = input("Give me a binary number\n")
        binaryNum = int(originalNum)
        break
    except:
        print("Input a integer please")


decimalNum = int(str(binaryNum), 2)

print(originalNum+" -> "+str(decimalNum))






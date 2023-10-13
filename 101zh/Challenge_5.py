nameList=[]

for i in range(5):
    nameList.append(input("Give me a name: "))

while True:
    try:
        nameIndex=int(input("Which name do you want to see? (1-5) "))
        print(nameList[nameIndex-1])
        break
    except:
        print("\nEnter a valid Integer")




import random

def randomChar(inName):
    userNameLen = len(inName)
    charPos = random.randint(1,userNameLen)
    print (str(userName[charPos]))
    return userName[charPos]
	
userName = input("type your first name")

print("\n")
print(userName + "\n" + str(randomChar(userName)))

exiter = input("Press any key to continue...")

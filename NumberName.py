#Assignment:
#Given the input of a user's name, print the user's name with a random character
#from the name on the lines above and below the reprinted name.


import random  #We need this for the to select the character from the name

def randomChar(inName):    
    userNameLen = len(inName)
    charPos = random.randint(1,userNameLen) #This function selects a random integer from 1-x where x is the length of the user's name
    print (str(userName[charPos])) #This line returns the character corresponding to the randomly selected
				   #position and prints the character on the line above the name
    return userName[charPos]
	
userName = input("type your first name")   #User inputs their name here

print("\n")
print(userName + "\n" + str(randomChar(userName))) #Print function only prints name and character below it

exiter = input("Press any key to exit...")

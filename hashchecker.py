hash_1 = input("Input first hash here") #User input of the first hash to compare
hash_2 = input("Input second hash here")#User input of the second hash to compare

if(hash_1.lower() == hash_2.lower()): #Checks for string equality
    print("The hashes match!")

elif(hash_1.lower() != hash_2.lower()):#Check for string inequality
    print("the hashes DON'T match! BEWARE!")

else:
    pass

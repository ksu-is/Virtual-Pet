#need prompt for pet type
#build  pet dictionary 
#give toys, feed pet, let game loop, while printing menu


pet = {"name":"", "type": "", "age": 0, "hunger": 0, "toys": []}

pettoys = {"cat": ["String", "Cardboard Box", "Scratching Post"], "dog": ["Frisbee","Tennis Ball", "Stick"], "fish": ["Undersea Castle", "Buried Treasure", "Coral"]}

def virtpet ():
    pettype = ""

    petops = list(pettoys.keys())

    while pettype not in petops:
        print("Please input pet you would like to have:")
        for option in petops:
            print(option)
        pettype = input("Please select from one of these pets: ")
    
    pet["type"] = pettype

    pet["name"] = input("What would you like to name your" + pet["type"] + "? ")

    print(pet)

virtpet()
#this initializes the pet game
#then it should ask you to choose and name your pet if its working correctly

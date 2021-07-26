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

#this initializes the pet game
#then it should ask you to choose and name your pet if its working correctly

def quitsim():
    print("By for now!")

def feedpet():
    print("Fed" + pet["name"])



def printMenu(menuops):
    optionkeys = list(menuops.keys())
    print("Here are your options: ")
    print("----------")
    for key in optionkeys:
        print(key + ":\t" + menuops[key]["text"])

def main():
    virtpet()

    menuops = {"Q": { "function": quitsim, "text": "Quit the game"}, "F": { "function": feedpet, "text": "Feed" + pet["name"] } }
    keepplaying = True
    while keepplaying:
        menuselect = ""
        while menuselect not in menuops.keys():
            print(menuops)
            menuselect = input("Which of thesee menu options would you like to use? ").upper()
        if menuselect == "Q":
            keepplaying = False 

    menuops[menuselect]["function"]()
main()
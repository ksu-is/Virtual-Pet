#need prompt for pet type
#build  pet dictionary 
#give toys, feed pet, let game loop, while printing menu


pet = {"name":"", "type": "", "age": 0, "hunger": 0, "toys": []}

pettoys = {"cat": ["String", "Cardboard Box", "Scratching Post"], "dog": ["Frisbee","Tennis Ball", "Stick"], "fish": ["Undersea Castle", "Buried Treasure", "Coral"]}

def quitsim():
  print("That's the end of the game! Thank you for playing the pet simulator!") 

def feedpet():
    newHunger = pet["hunger"] - 10
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] = newHunger
    print("Fed pet, their hunger is getting out of control")

def gettoy():
  toyChoices = pettoys[pet["type"]]
  toyNum = -1
  while toyNum < 0 or toyNum >= len(pettoys):
    print("Here are your toy choices: ")
    for i in range(len(toyChoices)):
      print(str(i) + ": " + toyChoices[i])
    
    toyNum = int(input("Please input your choice of pet toy: "))
  
  
  chosenToy = toyChoices[toyNum]

  
  pet["toys"].append(chosenToy)
  print("Nice! You chose: " + chosenToy + " for " + pet["name"] + ". Great pick!")

def virtpet ():
    pettype = ""

    petops = list(pettoys.keys())

    while pettype not in petops:
        print("Please input pet you would like to have:")
        for option in petops:
            print(option)
        pettype = input("Please select from one of these pets: ")
    
    pet["type"] = pettype

    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")

#this initializes the pet game
#then it should ask you to choose and name your pet if its working correctly

#Not only write a while loop but lets the user quit by hitting the q key

def printmenu(menuops):
    print()
    print("Here are your options: ")
    print("----------")

    for key in menuops:
        print(key + ":\t" + menuops[key]["text"])
    print()

#bug fix, not only was feedpet and quitsim not defined but once I defined it I could not get printmenu to show, just getting a long string of letters and numbers


def printStats():
  print()
  print("Your " + pet["type"] + " named " + pet["name"] + " had a great time playing with you!")
  print(pet["name"] + " is " + str(pet["age"]) + " days old")
  print(pet["name"] + " is currently at a hunger level of " + str(pet["hunger"]) + " out of 100!")
  print("You have " + str(len(pet["toys"])) + " toys! They are: ")
  for toy in pet["toys"]:
    print(toy)
  print() 
#added stats, pushed pass earlier error, will work on that later once I find a solution

def main():
    virtpet()

    menuops = {"Q": { "function": quitsim, "text": "Quit the game"}, "F": { "function": feedpet, "text": "Feed " + pet["name"] + "!"}, "G": { "function": gettoy, "text": "Get a toy for " + pet["name"] + "!"}, "P": { "function": playtoys, "text": "Play with " + pet["name"] + " and your toys!"} }


    keepplaying = True
    while keepplaying:
        menuselect = ""
        menuopskeys = list(menuops.keys())
        while menuselect not in menuopskeys:
            printmenu(menuops)
            menuselect = input("Which of thesee menu options would you like to use? ").upper()
            print()
        if menuselect == "Q":
            keepplaying = False 

        menuops[menuselect]["function"]()

main()
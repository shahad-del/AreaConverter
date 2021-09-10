print("Application launching...")
print("Available options to convert from:\n a. Ropani System\n b. Bigha system\n c. Square Feet\n d. Square Meter")
unitSystems = {
  "a": "Ropani System",
  "b": "Bigha System",
  "c": "Square Meter",
  "d": "Square Feet"
}
userOptions =list(unitSystems.keys())
userInput = input("unit you want to convert from: ")
counter = 0
while counter < 2:
    if userInput in userOptions:
        if userInput == userOptions[0]:
            userValue = input("eg. 0-3-4-4: \n")
            characters = list(userValue)
            area = []
            for i in range(len(characters)):
                if i % 2 == 0:
                    area.append(characters[i])
            totalArea =''.join(area)
            print(f"{totalArea[0]}Ropani {totalArea[1]}Aana {totalArea[2]}paisa {totalArea[3]}daam")
            for i in totalArea:
                ropani = int(totalArea[0]) * 256
                aana = int(totalArea[1]) * 16
                paisa = int(totalArea[2]) * 4
                totalDaam = ropani + aana + paisa + int(totalArea[3])
            totalDhur = totalDaam * 0.1174
            bigha = 0
            kattha = 0
            if totalDhur > 400:
                bigha += totalDhur // 400
                totalDhur = totalDhur % 400
            elif totalDhur > 20:
                    kattha += totalDhur // 20
                    totalDhur = totalDhur % 20
            print(f"{bigha}bigha {kattha}kattha {totalDhur:.2f}dhur")
            squareFeet = totalDaam * 21.39 
            squareMeter = totalDaam * 1.987179487179487
            print(f"{squareFeet} square feet")
            print(f"{squareMeter} squareMeter")

        elif userInput == userOptions[1]:
            userValue = input("eg. 0-4-4:")
        elif userInput == userOptions[2]:
            userValue = input("eg. 100:")
        elif userInput == userOptions[3]:
            userValue = input("eg. 200:")
    else:
       print("please enter valid option")
       break

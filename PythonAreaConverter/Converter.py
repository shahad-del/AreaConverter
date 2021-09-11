from ConvertHelpers import ConvertHelpers

print("Application launching...")
unitSystems = {
  "1": "Ropani System",
  "2": "Bigha System",
  "3": "Square Meter",
  "4": "Square Feet"
}
userOptions =list(unitSystems.keys())

ch = ConvertHelpers()


userInput = '0'
while userInput != '-1':
    print("Available options to convert from:\n 1. Ropani System\n 2. Bigha system\n 3. Square Feet\n 4. Square Meter\n type -1 to exit")
    userInput = input("unit you want to convert from: ")
    if userInput in userOptions:
        if userInput == userOptions[0]:

            areaValues = []
            while True:
                try:
                    userValue = input("eg. 0-4-4-3: \n")
                    areaValues = list(map(int, userValue.split('-')))
                    if len(areaValues) != 4:
                        raise Exception("Area must contain only 4 values")
                    break
                except:
                    print('Invalid input. Please retry.')

            ch.ConvertFromRopaniSystem(areaValues[0],areaValues[1],areaValues[2], areaValues[3])


        elif userInput == userOptions[1]:
            areaValues = []
            while True:
                try:
                    userValue = input("eg. 0-4-4: \n")
                    areaValues = list(map(int, userValue.split('-')))
                    if len(areaValues) != 3:
                        raise Exception("Area must contain only 3 values")
                    break
                except:
                    print('Invalid input. Please retry.')

            ch.ConvertFromBighaSystem(areaValues[0],areaValues[1],areaValues[2])

            


        elif userInput == userOptions[2]:
                userValue = []
                try:
                    userValue = int(input("eg. 100:\n"))
                except:
                    print('inavlid input.please type only numbers and without space')
                ch.converFromsquareFeet(userValue)       
        elif userInput == userOptions[3]:
            userValue = []
            try:
                userValue = input("eg. 200:\n")
            except:
                print('inavlid input.please type only numbers and without space')
            ch.converFromsquareMeter(userValue)   

    else:
        if userInput != '-1':
            print("please enter valid option")

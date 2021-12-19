myList = [44, 21, 53, 7, 109, 555, 29, 64, 32, 89, 2, 12]

number = input ('Please enter a number:')

try: 
    numberasnumber = int(number)
    lessnumbers= []
    # for i in range(0, len(myList)):
    #     print(myList[i])              -- If I want to know the index
    for i in myList:
        if numberasnumber > i:
            lessnumbers.append(i)

    print(f'The numbers that are less than the {numberasnumber} are: {lessnumbers}')
except:
    print('Invalid number')
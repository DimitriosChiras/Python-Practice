number = input ('Please enter a number:')

try: 
    numberasnumber = int(number)
    iseven = numberasnumber % 2 == 0

    if iseven:
        print(f'Number {numberasnumber} is even')
    else:
        print(f'Number {numberasnumber} is odd')

except:
    print('Invalid number')

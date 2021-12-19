name = input('Please enter your name:')
age = input ('Please enter your age:')

try: 

    ageasnumber = int(age)
    yearTurn100 = 2021 + (100 - ageasnumber)
    print(f'Dear {name} , you will turn 100 the year {yearTurn100}')

except:
    print('Invalid age')


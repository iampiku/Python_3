weight = float(input("Enter your weight : "))
unit = input("(L)bs or (K)g : ")

if(unit == 'L' or unit == 'l') :
    result = weight * 0.45
    print(f'Your weight in kg : {result}')

if(unit == 'K' or unit == 'k') :
    result = weight / 0.45
    print(f'Your weight in pounds : {result}') 
weight = float(input("Weight: "))
kilo_or_pounds = input('(K)g or (L)bs: ').upper()

if kilo_or_pounds == 'K':
    kilos = weight * 0.45;
    print(f"You are {kilos} kilos")
elif kilo_or_pounds == 'L':
    pouds = weight / 0.45;
    print(f'You are {pouds} pounds')
else:
    print('Enter a right option')

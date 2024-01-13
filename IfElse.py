woroodi = input('Marhale 1 yaa 2 ?')

if woroodi == '1':
    x = input('Please enter the amount :')
    x = int(x)

    if x > 10:
        print('The entered number is greater than 10 .')
        print('----------------------------------------')
    elif x == 10:
        print('The entered number is equal to 10 .')
        print('----------------------------------------')
    elif x < 10:
        print('The entered number is less than 10 .')
        print('----------------------------------------')
    else:
        print('The entered phrase is incorrect.')
        print('----------------------------------------')

    print('----------------------------------------')
elif woroodi == '2':
    z = input('Please enter the amount :')
    z = int(z)

    if z > 0:
        print('The entered number is greater than 0 .')
        print('----------------------------------------')
    elif z == 0:
        print('The entered number is equal to 0 .')
        print('----------------------------------------')
    elif z < 0:
        print('The entered number is less than 0 .')
        print('----------------------------------------')
    else:
        print('The entered phrase is incorrect.')
        print('----------------------------------------')

    print('----------------------------------------')
else:
    print('The entered phrase is incorrect.')
